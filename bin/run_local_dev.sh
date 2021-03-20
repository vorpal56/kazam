
cd data; 
cp -ua icons hicolor
cd hicolor
ln -s . scalable/apps >/dev/null 2>&1
find -iname '*.png' -type f -printf "ln -s '%f' '%P-symbolic'\n" | sed -e 's#.png-symbolic#-symbolic.png#' | sh >/dev/null 2>&1

cd ../../bin
export PYTHONPATH=..
./kazam "$@"

