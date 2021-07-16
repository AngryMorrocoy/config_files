" Indentation config

setlocal shiftwidth=4
setlocal tabstop=4
setlocal smartindent
setlocal foldmethod=indent
let g:NERDSpaceDelims=0

" Run code command

noremap <buffer> <Leader>r :!python3 '%' <Enter>
noremap <buffer> <Leader>dr :!python3 '%'
noremap <buffer> <Leader>p :Autopep8 <cr>
nmap <buffer> <Leader>C :w<CR>:!autoflake -i --remove-all-unused-imports --remove-duplicate-keys --remove-unused-variables %<CR>:!black %<CR><CR>:e!<CR>

