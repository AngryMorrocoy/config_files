" Indentation config

setlocal shiftwidth=4
setlocal tabstop=4
setlocal smartindent

" Run code command

noremap <Leader>r :!python3 '%' <Enter>
noremap <Leader>dr :!python3 '%'
noremap <Leader>A :Autopep8 <cr>

