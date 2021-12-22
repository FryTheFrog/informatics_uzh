git init
printf "aaa" > a.txt
printf "bbb" > b.txt
git add a.txt
git add b.txt
git commit -m "Add files a.txt and b.txt"
printf "\nb2" >> b.txt
git add b.txt
git commit -m "Add second line to b.txt"