-- Renders small epistemic-status badges under a post's title, driven by
-- frontmatter fields. Each dimension below is independent and optional: a
-- badge only appears if its frontmatter field is set to a recognized value,
-- so untagged posts (and non-post pages) render unchanged. `freshness` is
-- the one exception -- it's derived automatically from the post's `date`.

local dimensions = {
  {
    key = "confidence",
    note_key = "confidence-note",
    class_prefix = "badge-confidence-",
    labels = {
      low = { emoji = "🌫️", text = "Low confidence", note = "Casual post, not carefully checked." },
      medium = { emoji = "⛅", text = "Medium confidence", note = "Reasonably confident." },
      high = { emoji = "☀️", text = "High confidence", note = "Highly confident in the claims." },
    },
  },
  {
    key = "ai-involvement",
    note_key = "ai-involvement-note",
    class_prefix = "badge-ai-",
    labels = {
      assisted = { emoji = "🤖", text = "AI-assisted", note = "AI helped with research, editing, or drafting parts of this." },
      ["co-written"] = { emoji = "🤖", text = "AI co-written", note = "Substantial portions were AI-generated or AI-co-authored." },
    },
  },
  {
    key = "effort",
    note_key = "effort-note",
    class_prefix = "badge-effort-",
    labels = {
      low = { emoji = "✏️", text = "Quick post", note = "Written quickly, without much editing or fact-checking." },
      medium = { emoji = "🔧", text = "Moderate effort", note = "A normal amount of drafting and revision." },
      high = { emoji = "💎", text = "High effort", note = "Carefully researched, drafted, and revised." },
    },
  },
  {
    key = "originality",
    note_key = "originality-note",
    class_prefix = "badge-originality-",
    labels = {
      low = { emoji = "🪞", text = "Low originality", note = "" },
      medium = { emoji = "🧩", text = "Medium originality", note = "" },
      high = { emoji = "💡", text = "High originality", note = "" },
    },
  },
}

local FRESHNESS_WINDOW_DAYS = 60

local MONTH_NUMBERS = {
  January = 1, February = 2, March = 3, April = 4, May = 5, June = 6,
  July = 7, August = 8, September = 9, October = 10, November = 11, December = 12,
}

local function meta_to_str(v)
  if v == nil then return nil end
  return pandoc.utils.stringify(v)
end

-- By the time this filter runs, Quarto has already reformatted `date:` from
-- YAML (e.g. "2026-07-25" or "2026-07-25T22:00Z") into a human-readable
-- string (e.g. "July 25, 2026") for display. Parse that instead of the raw
-- YAML value.
local function parse_post_date(date_str)
  local y, m, d = date_str:match("^(%d%d%d%d)%-(%d%d)%-(%d%d)")
  if y then
    return tonumber(y), tonumber(m), tonumber(d)
  end

  local month_name, day, year = date_str:match("^(%a+) (%d+), (%d+)$")
  if month_name and MONTH_NUMBERS[month_name] then
    return tonumber(year), MONTH_NUMBERS[month_name], tonumber(day)
  end

  return nil
end

local function make_badge(class, emoji, label, tooltip)
  return pandoc.Span(
    { pandoc.Str(emoji .. " " .. label) },
    pandoc.Attr("", { "post-badge", class }, { title = tooltip })
  )
end

local function freshness_badge(meta)
  local date_str = meta_to_str(meta.date)
  if not date_str then return nil end

  local y, m, d = parse_post_date(date_str)
  if not y then return nil end

  local post_time = os.time({ year = y, month = m, day = d, hour = 12 })
  local days_old = os.difftime(os.time(), post_time) / 86400
  if days_old < 0 or days_old >= FRESHNESS_WINDOW_DAYS then return nil end

  return make_badge(
    "badge-fresh", "🌱", "New",
    "Published within the last " .. FRESHNESS_WINDOW_DAYS .. " days."
  )
end

function Pandoc(doc)
  local meta = doc.meta
  local badges = {}

  for _, dim in ipairs(dimensions) do
    local value = meta_to_str(meta[dim.key])
    local info = value and dim.labels[value]
    if info then
      local note = meta_to_str(meta[dim.note_key]) or info.note
      table.insert(badges, make_badge(dim.class_prefix .. value, info.emoji, info.text, note))
    end
  end

  local fresh = freshness_badge(meta)
  if fresh then table.insert(badges, fresh) end

  if #badges == 0 then
    return doc
  end

  local inlines = {}
  for i, b in ipairs(badges) do
    if i > 1 then table.insert(inlines, pandoc.Space()) end
    table.insert(inlines, b)
  end

  local badge_div = pandoc.Div({ pandoc.Para(inlines) }, pandoc.Attr("", { "post-badges" }))
  table.insert(doc.blocks, 1, badge_div)
  return doc
end
