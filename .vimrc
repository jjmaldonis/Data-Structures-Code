set tabstop=4
set shiftwidth=4
set softtabstop=4

set expandtab
set smarttab

set autoindent

filetype plugin indent on
if has("autocmd")
  augroup filetypedetect
    au FileType python    setl et
  augroup END
endif

set nu
set background=dark
