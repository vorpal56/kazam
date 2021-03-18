
cd data; 
cp -ua icons hicolor
cd hicolor
find -iname '*.png' -type f -printf "ln -s '%f' '%P-symbolic'\n" | sed -e 's#.png-symbolic#-symbolic.png#' | sh >/dev/null 2>&1

cd ../../bin
export PYTHONPATH=..
./kazam

