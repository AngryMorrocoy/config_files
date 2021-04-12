" Indentacion config

setlocal shiftwidth=2
setlocal tabstop=2
setlocal expandtab

" Run command
au FileType javascript setlocal foldmethod=syntax
noremap <buffer> <Leader>r :!clear; node '%' <cr>

