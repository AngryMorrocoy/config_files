setlocal expandtab
setlocal shiftwidth=4
setlocal tabstop=4
setlocal smartindent

" Functions refered to compilation and execution of code

function! Compile()
    :!f='%:p' && gcc ${f} -o ${f\%.c}
endfunction

function! Run()
    :!clear && f='%:p' && ${f\%.c}
endfunction

function! Com_run()
    silent execute ":!clear"
    execute "call Compile()"
    if v:shell_error == 0
        execute 'call Run()'
    else
        execute 'echo "No se pudo compilar"'
    endif
endfunction

" Forma rapida de compilar y ejecutar

noremap <buffer> <Leader>r :call Run() <Enter>
noremap <buffer> <leader>c :call Compile() <cr>
noremap <buffer> <leader><leader>r :call Com_run() <cr>

