#!/bin/sh

# Do your user specific stuff like overriding env variables here

# Nvchad
if [ ! -d "$HOME/.config/nvim" ]; then
  git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1
  mkdir -p ~/.config/nvim/lua/custom
  echo "vim.opt.relativenumber = true" > ~/.config/nvim/lua/custom/init.lua
fi


if [ ! -d "$HOME/hack/history" ]; then
  mkdir -p "$HOME/hack/history"
fi

# lunarvim
#export PATH=~/.npm-global/bin:$PATH
#if [ ! -d "$HOME/.config/lvim" ]; then
#  mkdir -p $HOME/.npm-global && \
#  npm config set prefix "$HOME/.npm-global" && \
#  npm -g install yarn && \
#  wget -O /tmp/lunar-install.sh https://raw.githubusercontent.com/lunarvim/lunarvim/master/utils/installer/install.sh && \
#  yes "y" | bash /tmp/lunar-install.sh && \
#  rm /tmp/lunar-install.sh && \
#
#  cat >> "$HOME/.config/lvim/config.lua" << EOL
#-- ##################################################
#-- Run :PackerInstall on first run to install plugins
#-- ##################################################
#
#local formatters = require "lvim.lsp.null-ls.formatters"
#formatters.setup {
#  { command = "shfmt", filetypes = { "sh" } },
#}
#
#local linters = require "lvim.lsp.null-ls.linters"
#linters.setup {
#  { command = "shellcheck", filetypes = { "sh" } },
#}
#
#vim.opt.relativenumber = true
#
#lvim.plugins = {
#  {"phaazon/hop.nvim"},
#  {"f-person/git-blame.nvim"},
#  {"windwp/nvim-ts-autotag"},
#  {"folke/trouble.nvim", cmd = "TroubleToggle"},
#  {"folke/todo-comments.nvim"},
#  {"norcalli/nvim-colorizer.lua"}
#}
#
#local _, hop = pcall(require, "hop")
#hop.setup()
#vim.api.nvim_set_keymap("", "s", ":HopChar2<cr>", { silent = true })
#vim.api.nvim_set_keymap("", "S", ":HopWord<cr>", { silent = true })
#
#lvim.builtin.treesitter.autotag = {
#  enable = true,
#  filetypes = {'html', 'xml', 'javascript', 'javascriptreact', 'typescriptreact', 'svelte', 'vue', 'rescript'},
#}
#
#-- local _, autotag = pcall(require, "nvim-ts-autotag")
#-- autotag.setup()
#
#local _, todo_comments = pcall(require, "todo-comments")
#todo_comments.setup()
#
#local _, colorizer = pcall(require, "colorizer")
#colorizer.setup({ "*" }, {
#    RGB = true, -- #RGB hex codes
#    RRGGBB = true, -- #RRGGBB hex codes
#    RRGGBBAA = true, -- #RRGGBBAA hex codes
#    rgb_fn = true, -- CSS rgb() and rgba() functions
#    hsl_fn = true, -- CSS hsl() and hsla() functions
#    css = true, -- Enable all CSS features: rgb_fn, hsl_fn, names, RGB, RRGGBB
#    css_fn = true, -- Enable all CSS *functions*: rgb_fn, hsl_fn
#  })
#
#vim.g.gitblame_enabled = 1
#vim.g.gitblame_message_template = "<summary> • <date> • <author>"
#vim.g.gitblame_highlight_group = "LineNr"
#EOL
#
#  echo "#########################################################"
#  echo "Open lvim (e) and run :PackerInstall and :PackerCompile"
#  echo "#########################################################"
#  echo ""
#fi

#npm list --depth 1 -g neovim > /dev/null || npm install -g neovim
pip3 show pynvim > /dev/null || sudo python3 -m pip install pynvim

# install prettier lsd
if ! command -v lsd > /dev/null; then
  wget -O /tmp/lsd.deb "$(curl -s https://api.github.com/repos/Peltoche/lsd/releases/latest | jq -r '.assets[].browser_download_url' | grep 'lsd_.*amd64')" 
  sudo apt install /tmp/lsd.deb 
  rm /tmp/lsd.deb
fi

# get ranger conf
[ ! -f "$HOME/.config/ranger/rc.conf" ] && mkdir -p "$HOME/.config/ranger/" && curl https://gist.githubusercontent.com/braunbearded/de021eda8704ccc98c19e12a15d57ca8/raw/c0b374b0c23582acda72d0a0b4cc5cbfd7a8729e/rc.conf > "$HOME/.config/ranger/rc.conf"

echo "# empty" > "$HOME/.zshrc"

echo ""
echo "#########################################################################"
cat $HOME/.config/commands.txt
echo "#########################################################################"

# Installing reconftw results in wired version issues
#if [ ! -d "$HOME/.reconftw" ]; then
#    git clone https://github.com/six2dez/reconftw.git "$HOME/.reconftw"
#    cd .reconftw
#    chmod +x *.sh
#    ./install.sh
#    cd "$HOME"
#fi

