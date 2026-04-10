local function set_file_mark(mark, filepath)
	local abs_path = vim.fn.fnamemodify(filepath, ":p")
	local bufnr = vim.fn.bufadd(abs_path)
	vim.fn.setpos("'" .. mark, { bufnr, 1, 1, 0 })
end

local function clear_global_marks()
	-- Loop through A (65) to Z (90)
	for i = string.byte("A"), string.byte("Z") do
		local mark = string.char(i)
		vim.api.nvim_del_mark(mark)
	end
end
clear_global_marks()

set_file_mark("R", "./21_rabbit_mq/cmd/client/main.go")
