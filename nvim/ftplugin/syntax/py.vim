" Indentation config

setlocal shiftwidth=4
setlocal tabstop=4
setlocal smartindent

" Run code command

noremap <Leader>r :!clear; python3 '%' <Enter>
noremap <Leader>dr :!clear; python3 '%'

