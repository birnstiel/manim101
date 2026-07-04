local str = pandoc.utils.stringify

local template_fold_p1 = [[
<details>
  <summary>
  %s
  </summary>
]]

local template_fold_p2 = [[
</details>
]]

local function wrap_in_details(blocks, code_summary)
  local result = {
    pandoc.RawBlock('html', string.format(template_fold_p1, code_summary)),
  }

  for _, block in ipairs(blocks) do
    table.insert(result, block)
  end

  table.insert(result, pandoc.RawBlock('html', template_fold_p2))
  return result
end

local function strip_quarto_options(code)
  local code_lines = {}
  local code_summary = 'Show code'
  local should_fold = false

  for line in code:gmatch('[^\r\n]+') do
    local folded = line:match('^#%|%s*code%-fold:%s*true%s*$')
    if folded then
      should_fold = true
    else
      local summary = line:match('^#%|%s*code%-summary:%s*"?(.-)"?%s*$')
      if summary then
        code_summary = summary
      elseif not line:match('^#%|') then
        table.insert(code_lines, line)
      end
    end
  end

  return should_fold, code_summary, table.concat(code_lines, '\n')
end

function CodeBlock(el)
  if el.attributes['code-fold'] then
    local code_summary = str(el.attributes['code-summary'])
    return wrap_in_details({ el }, code_summary)
  end

  local should_fold, code_summary, code = strip_quarto_options(el.text)
  if should_fold then
    local folded_block = pandoc.CodeBlock(code, el.attr)
    return wrap_in_details({ folded_block }, code_summary)
  end
end

function Div(el)
  if el.attributes['code-fold'] then
    local code_summary = str(el.attributes['code-summary'])
    return wrap_in_details(el.content, code_summary)
  end
end