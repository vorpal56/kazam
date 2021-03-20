
cd data; 
cp -ua icons hicolor
cd hicolor
ln -s . scalable/apps >/dev/null 2>&1
find -type f -printf "%f,,,%P-sym\n" | perl -ne 's#\s*##; @x=split(/,,,/);if($x[0]!~m#-symbolic# && $x[1]=~s#\.(svg|png)-sym$#-symbolic\.\1#) { symlink($x[0],$x[1]); }' 

cd ../../bin
export PYTHONPATH=..
./kazam "$@"

