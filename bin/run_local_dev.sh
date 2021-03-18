
cd data; 
cp -a icons hicolor
cd hicolor
find -iname '*.png' -type f -printf "ln -s '%f' '%P-symbolic'\n" | sed -e 's#.png-symbolic#-symbolic.png#' | sh

