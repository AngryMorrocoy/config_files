" __  __ ____  _      __     ___
"|  \/  |  _ \( )___  \ \   / (_)_ __ ___  _ __ ___
"| |\/| | |_) |// __|  \ \ / /| | '_ ` _ \| '__/ __|
"| |  | |  _ <  \__ \   \ V / | | | | | | | | | (__
"|_|  |_|_| \_\ |___/    \_/  |_|_| |_| |_|_|  \___|
" --- IMPORTANT  ---
set nocompatible  " Disables compatibility with vi
" --- IMPORTANT  ---

if has("autocmd")

  " Put these in an autocmd group, so that we can delete them easily.
  augroup vimrcEx
  au!

  " For all text files set 'textwidth' to 78 characters.
  autocmd FileType text setlocal textwidth=78

  augroup END

endif

augroup vimStartup
    au!

    " When editing a file, always jump to the last known cursor position.
    " Don't do it when the position is invalid
    autocmd BufReadPost *
      \ if line("'\"") >= 1 && line("'\"") <= line("$") && &ft !~# 'commit'
      \ |   exe "normal! g`\""
      \ | endif

augroup END

" Fuck trailing whitespaces
autocmd BufWritePre * %s/\s\+$//e
" More clear split lines
autocmd Colorscheme * highlight VertSplit ctermbg=NONE guibg=NONE guifg=fg
" Saves the colorscheme default guibg
autocmd Colorscheme * let g:default_guibg=synIDattr(hlID("Normal"), "bg#")
" Saves the colorscheme default ctermbg
autocmd Colorscheme * let g:default_ctermbg=synIDattr(hlID("Normal"), "bg")
" Terminal stuff
au TermOpen * setlocal listchars= nonumber norelativenumber
au TermOpen * startinsert
au BufEnter,BufWinEnter,WinEnter term://* startinsert
au BufLeave term://* stopinsert
" Closes the terminal if is the only one open
au BufEnter * if (winnr("$") == 1 && bufname() =~ "^term://*") | q | endif

" Functions and commands

function! Openterm()
    " Opens a terminal
    let cur_dir = execute(":pwd")[1:]
    echo cur_dir
    execute "!alacritty --working-directory ".cur_dir."&"
endfunc

function! ToggleBackgroundTransparency()
    " Toggles the background transparency
    let actual_ctermbg = synIDattr(hlID("Normal"), "bg")
    let actual_guibg = synIDattr(hlID("Normal"), "bg#")
    if actual_ctermbg != "" && actual_guibg != ""
        highlight Normal ctermbg=NONE guibg=NONE
    else
        execute 'highlight Normal guibg='.g:default_guibg
    endif
endf

" Copy to clipboard the path of he file current file
command! CopyFilePath :!echo "%:p" | xclip -i -sel c
" Toggles the background transparency
command! ToggleBackgroundTransparency call ToggleBackgroundTransparency()
" Command to open splitted term
command! -nargs=* T split | resize 12 |terminal <args>

" Setters

let mapleader=","  " Mapleader, for commands and stuff
set fillchars+=vert:¦  " Vertsplit character

set termguicolors " Use the colors of the terminal

set noswapfile " Disable the swapfiles

set mouse=n  " Disable mouse

set nobackup  " Chinguen a su madre los backups

set undodir=~/.local/share/vim/undodir/  " Directory where undofiles will go
set undofile  " Activate the undofile

set backspace=indent,eol,start  " Allows backspace on everything. Insert mode

set history=50  " keep 50 lines of command line history
set ruler  " show the cursor position all the time
set wildmenu  " display completion matches in a status line

set ttimeout  " time out for key codes
set ttimeoutlen=100  " wait up to 100ms after Esc for special key

set splitright " When split the window, do it to the right
set splitbelow " When split the window, do it below

set smartindent  " Configures indentantion
set expandtab  " Tabulations are spaces
set shiftwidth=4  " Width of tabulation is 4 by default
set tabstop=4  " ^

set ignorecase " Makes the search case insensitive

set showtabline=2 " Always shows the tabline
set number  " View linenumbers
set relativenumber  " View relative numbers
set numberwidth=3  " Length of the shown numbers
set cursorline  " Highlight the line where cursor is
set scrolloff=10  " Keeps 10 lines when scroling on file
set encoding=utf-8  " Set default encoding to utf-8

set conceallevel=1  " Conceallevel

set colorcolumn=110  " Displays a margin at 110 characters

set title  " Displays the opened file path as terminal title
set laststatus=2 " Type of the status bar required for lightline/airline
set noshowmode  " Doesn't show the status bar
set noshowcmd  " Doesn't show the command that is being tiped

set completeopt=menuone  " Changes the way completion is showed

syntax on  " Enable syntax highlighting
filetype plugin on  " Enables filetype detection

let g:rainbow_active = 1

" Filetype definition

au FileType python source ~/.config/nvim/ftplugin/syntax/py.vim  " Python

au FileType javascript source ~/.config/nvim/ftplugin/syntax/js.vim  " Javascript
au FileType typescript source ~/.config/nvim/ftplugin/syntax/js.vim  " Typescript
au FileType typescript source ~/.config/nvim/ftplugin/syntax/json.vim  " Json

au FileType c source ~/.config/nvim/ftplugin/syntax/c.vim  " C
au FileType cpp source ~/.config/nvim/ftplugin/syntax/cpp.vim  " C++

au FileType java source ~/.config/nvim/ftplugin/syntax/java.vim  " C

au FileType html* source ~/.config/nvim/ftplugin/syntax/html.vim " Html
au FileType xml source ~/.config/nvim/ftplugin/syntax/html.vim " Html

au FileType css source ~/.config/nvim/ftplugin/syntax/css.vim " Css
au FileType cs source ~/.config/nvim/ftplugin/syntax/cs.vim " Css

" !Load maps
source ~/.config/nvim/ftplugin/maps.vim
" Load maps!

if version >= 800 " If not started as vi
    " Loads coc
    packadd coc.nvim-release
    " Coc's config
        if has('nvim')
          inoremap <silent><expr> <c-space> coc#refresh()
        else
          inoremap <silent><expr> <c-@> coc#refresh()
        endif

        let g:coc_disable_startup_warning = 1
        let b:coc_disable_transparent_cursor = 1

        nnoremap <silent> <leader>d :call <SID>show_documentation()<CR>

        function! s:show_documentation()
          if (index(['vim','help'], &filetype) >= 0)
            execute 'h '.expand('<cword>')
          elseif (coc#rpc#ready())
            call CocActionAsync('doHover')
          else
            execute '!' . &keywordprg . " " . expand('<cword>')
          endif
        endfunction

        inoremap <silent><expr> <TAB>
              \ pumvisible() ? "\<C-n>" :
              \ <SID>check_back_space() ? "\<TAB>" :
              \ coc#refresh()
        inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

        function! s:check_back_space() abort
          let col = col('.') - 1
          return !col || getline('.')[col - 1]  =~# '\s'
        endfunction
endif

" Matchup
    let g:matchup_matchparen_deferred = 1
    let g:matchup_matchparen_hi_surround_always = 1
    let g:matchup_matchparen_offscreen = {'method': 'popup'}

" Indentline
    let g:indentLine_char = "|"
    let g:indentLine_conceallevel = "1"
    let g:indentLine_color_term = 181
    let g:indentLine_first_char = '.'
    let g:indentLine_showFirstIndentLevel = 1

" Vim-polyglot
    let g:vim_json_syntax_conceal = 0
    let g:vim_markdown_conceal = 0
    let g:vim_markdown_conceal_code_blocks = 0
" Nerdtree
    autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
    " If another buffer tries to replace NERDTree, put in the other window, and bring back NERDTree.
    autocmd BufEnter * if bufname('#') =~ 'NERD_tree_\d\+' && bufname('%') !~ 'NERD_tree_\d\+' && winnr('$') > 1 |
    " Open the existing NERDTree on each new tab.
        \ let buf=bufnr() | buffer# | execute "normal! \<C-W>w" | execute 'buffer'.buf | endif
    autocmd BufWinEnter * silent NERDTreeMirror

    let g:NERDTreeMapActivateNode = "l"
    let g:NERDTreeWinPos = "right"

" CtrlP
    " Command to use when ctrl+p is pressed
    let g:ctrlp_map='<c-p>'
    let g:ctrlp_cmd='CtrlPBuffer'
    let g:ctrlp_working_path_mode='ra'

    " Ignore son files or dirs
    let g:ctrlp_custom_ignore = {
      \ 'dir':  '\v[\/]\.?(git|hg|svn|__pycache__|node_modules|.vscode)$',
      \ 'file': '\v\.(exe|so|dll)$',
      \ 'link': '',
      \ }

    " Search using regex
    let g:ctrlp_regexp=1

    " Doesn't searchs by file name
    let g:ctrlp_by_filename=0

    " Look and feel
    let g:ctrlp_match_window='bottom,order:btt,min:1,max:10,results:30'

    " Opens new tabs at the very end of 'list"
    let g:ctrlp_tabpage_position="l"

    " Show hidden files
    let g:ctrlp_show_hidden=1

    " Setting max_depth and max_files
    let g:ctrlp_max_depth=20
    let g:ctrlp_max_files=1000

" Airline
    let g:airline#extensions#tabline#enabled=1
    let g:airline#extensions#tabline#left_sep = ''
    let g:airline#extensions#tabline#left_alt_sep = ' '
    let g:airline#extensions#tabline#formatter = 'unique_tail'
    let g:airline#extensions#tabline#show_buffers = 0

    let g:airline#extensions#branch#enabled=1

    let g:airline_powerline_fonts=1

    let g:airline_theme="ayu"

" Emmet
    let g:user_emmet_leader_key='<C-s>'


" UltiSnippets
    let g:UltiSnipsExpandTrigger="<C-s><cr>"
    let g:UltiSnipsListSnippets="<C-s><tab>"


" Startify

let g:ascii = [
            \ '                ┌────────────────────────────┐            ',
            \ '                │                            │            ',
            \ '                │        m    m mmmmm        │            ',
            \ '                │        ##  ## #   "#       │            ',
            \ '                │        # ## # #mmmm"       │            ',
            \ '                │        # "" # #   "m       │            ',
            \ '                │        #    # #    "       │            ',
            \ '                │                            │            ',
            \ '                │                            │            ',
            \ '                └────────────────────────────┘            ',
            \ '----------------------------------------------------------',
            \ '__     _____ __  __ _ ____    ____ _____  _    ____ _____',
            \ '\ \   / /_ _|  \/  ( ) ___|  / ___|_   _|/ \  |  _ \_   _|',
            \ ' \ \ / / | || |\/| |/\___ \  \___ \ | | / _ \ | |_) || |',
            \ '  \ V /  | || |  | |  ___) |  ___) || |/ ___ \|  _ < | |',
            \ '   \_/  |___|_|  |_| |____/  |____/ |_/_/   \_\_| \_\|_|'
            \ ]

let g:startify_custom_header =
            \ 'startify#pad(g:ascii)'


let g:startify_bookmarks = [
    \ { 'C': '~/Codes/' },
    \ { 'J': '~/IdeaProjects' },
    \ { 'c': '~/.config' },
    \ { 'm': '/run/media/Shared/Shared/Music/canciones.txt' }
    \ ]
let g:startify_files_number=15
let g:startify_padding_left=10

let g:startify_lists = [
    \ { 'type': 'bookmarks', 'header': ['        -Bookmarks-']     },
    \ { 'type': 'files',     'header': ['        -MRU-']           },
    \ { 'type': 'dir',       'header': ['        -MRU- '.getcwd()] },
    \ { 'type': 'commands',  'header': ['        -Commands-']      },
    \ ]

" Vim-rainbow
let g:rainbow_active = 1 "set to 0 if you want to enable it later via :RainbowToggle

map Q gq  " Don't use ex mode

" Colorscheme configuration

if version >= 800
    source ~/.config/nvim/theme.vim
endif

