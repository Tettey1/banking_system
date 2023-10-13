let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/CBS/CBS_API
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +1 ~/CBS/CBS_API
badd +63 CBS_API/settings.py
badd +1 CBS_API/celery.py
badd +1 IT_Managers/__init__.py
badd +5 CBS_API/__init__.py
badd +2 IT_Managers/models.py
badd +1 IT_Managers/common.py
badd +183 IT_Managers/utils.py
badd +2 IT_Managers/tasks.py
badd +1 CBS_API/wsgi.py
badd +1 CBS_API/asgi.py
badd +1 manage.py
badd +1 Managers/__init__.py
badd +6 Managers/apps.py
badd +1 config/settings.json
badd +1 Managers/models.py
badd +3 Managers/common.py
badd +1 Managers/managers.py
badd +13 Managers/custom_backend.py
badd +5 Managers/admin.py
badd +1 Managers/views.py
badd +17 Managers/api_views/signup.py
badd +95 Managers/decorators.py
badd +1 Managers/urls.py
badd +22 CBS_API/urls.py
badd +127 Managers/utils.py
badd +17 Managers/api_views/login.py
badd +61 Managers/api_views/otp_verification.py
badd +1 config/apache.conf
badd +17 config/alert.ini
badd +2 config/cbs.ini
badd +19 Managers/api_views/otp_resend.py
badd +65 Managers/api_views/password_reset.py
badd +1 Managers/api_views/password_reset_confirmation.py
badd +1 Managers/tasks.py
badd +1 Managers/api_views/staffs.py
badd +30 Managers/api_views/staff_details.py
badd +20 Managers/api_views/roles.py
badd +1 Customers/models.py
badd +1 Customers/api_views/user_setup.py
badd +7 Customers/urls.py
badd +4 Customers/admin.py
badd +31 Customers/api_views/customers.py
badd +76 Customers/api_views/customer_details.py
badd +35 Managers/api_views/token_verification.py
badd +1 accounts/models.py
badd +9 accounts/apps.py
badd +10 accounts/signals.py
badd +7 accounts/utils.py
badd +5 accounts/admin.py
badd +4 deposits/models.py
badd +22 transactions/models.py
badd +1 transactions/api_views/deposit.py
badd +3 transactions/decorators.py
badd +10 transactions/urls.py
badd +7 transactions/admin.py
badd +5 deposits/admin.py
badd +13 config/nginx.conf
badd +21 config/cbs2.ini
badd +6 transactions/api_views/transactions.py
badd +8 withdrawals/models.py
badd +41 withdrawals/api_views/withdrawal.py
badd +5 withdrawals/admin.py
badd +17 accounts/api_views/account.py
badd +4 accounts/urls.py
argglobal
%argdel
$argadd ~/CBS/CBS_API
set stal=2
tabnew +setlocal\ bufhidden=wipe
tabnew +setlocal\ bufhidden=wipe
tabrewind
edit CBS_API/settings.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe '1resize ' . ((&lines * 25 + 17) / 35)
exe '2resize ' . ((&lines * 6 + 17) / 35)
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 232 - ((12 * winheight(0) + 12) / 25)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 232
normal! 0
lcd ~/CBS/CBS_API
wincmd w
argglobal
enew
balt ~/CBS/CBS_API/CBS_API/settings.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
lcd ~/CBS/CBS_API
wincmd w
exe '1resize ' . ((&lines * 25 + 17) / 35)
exe '2resize ' . ((&lines * 6 + 17) / 35)
tabnext
edit ~/CBS/CBS_API/accounts/api_views/account.py
argglobal
balt ~/CBS/CBS_API/CBS_API/urls.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 11 - ((10 * winheight(0) + 16) / 32)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 11
normal! 072|
lcd ~/CBS/CBS_API
tabnext
edit ~/CBS/CBS_API/Customers/api_views/customers.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe '1resize ' . ((&lines * 28 + 17) / 35)
exe '2resize ' . ((&lines * 3 + 17) / 35)
argglobal
balt ~/CBS/CBS_API/transactions/api_views/transactions.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 39 - ((22 * winheight(0) + 14) / 28)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 39
normal! 0
lcd ~/CBS/CBS_API
wincmd w
argglobal
enew
balt ~/CBS/CBS_API/Managers/api_views/signup.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
lcd ~/CBS/CBS_API
wincmd w
exe '1resize ' . ((&lines * 28 + 17) / 35)
exe '2resize ' . ((&lines * 3 + 17) / 35)
tabnext 1
set stal=1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
