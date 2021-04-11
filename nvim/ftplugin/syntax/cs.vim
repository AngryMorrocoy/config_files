setlocal expandtab
setlocal shiftwidth=4
setlocal tabstop=4
setlocal smartindent

function! Compile()
    :!f="%:p" && g++ ${f} -o ${f\%.cpp}
endfunction

function! Run()
    :!clear && f="%:p" && ${f\%.cpp}
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

" C# works with omnisharp, use omnisharp moves instead of coc

nmap <buffer> <silent>   <leader>g :call CocAction("jumpDefinition") <cr>
nmap <buffer> <silent>   <leader>R :call CocAction("jumpReferences") <cr>
nmap <buffer> <leader>.r :OmnisharpRename

"noremap <Leader>r :call Run() <Enter>
"noremap <leader>c :call Compile() <cr>
"noremap <leader><leader>r :call Com_run() <cr>

