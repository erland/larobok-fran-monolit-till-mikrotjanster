-- PDF: numrerade H1 får kompakt tvådelad kapitelstart; övriga H1 (t.ex. Inledning) blir onumrerade kapitel.
local current_chapter = nil
function Header(el)
  if el.level == 2 and current_chapter == '13' and pandoc.utils.stringify(el.content):match('^Vem ansvarar för helhetsbilden%?') then
    return {pandoc.RawBlock('latex', '\\enlargethispage{3\\baselineskip}'), el}
  end
  if el.level ~= 1 then return nil end
  local text = pandoc.utils.stringify(el.content)
  local number, title = text:match("^%s*(%d+)%.%s+(.+)%s*$")
  if not number then number, title = text:match("^%s*[Kk]apitel%s+(%d+):%s*(.+)%s*$") end
  if number then
    current_chapter = number
    local blocks = pandoc.read(title, "markdown").blocks
    local inlines = (#blocks > 0 and blocks[1].content) or {pandoc.Str(title)}
    local title_tex = pandoc.write(pandoc.Pandoc({pandoc.Para(inlines)}), "latex"):gsub("%s+$", "")
    return pandoc.RawBlock("latex", "\\bookchapter{" .. number .. "}{" .. title_tex .. "}")
  end
  local escaped = pandoc.write(pandoc.Pandoc({pandoc.Para(el.content)}), "latex"):gsub("%s+$", "")
  return pandoc.RawBlock("latex", "\\bookfrontchapter{" .. escaped .. "}")
end
