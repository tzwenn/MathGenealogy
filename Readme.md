Are you studying math and always wanted to know your academical "heritage?"

The [Mathematics Genealogy Project](http://genealogy.math.ndsu.nodak.edu/) started a database providing currently (June 2011) about 150000 records of mathematicians, their degrees and advisors of their theses.

Since they don't provide a database dump this small tool crawls the (as statical assumed) website and offers you the possibility of visualizing the acedemic family tree of your lecturer or advisor using [GraphVIZ](http://www.graphviz.org/).

##Usage##

It's not very straightforward yet, but if you like to use this programm visit the Mathematics Genealogy Project's [website](http://genealogy.math.ndsu.nodak.edu/) and search for the desired mathematician. Copy his or her id from the URL (e.g. Leonhard Euler) would be identified by `id.php?id=38586`. Let the program first download his ancestry, then generate a `.dot` file.

```bash
$ ./genealogy --search 38586
$ ./genealogy --display 38586 > euler.dot
``

The next step would be using one of the GraphVIZ-tools like `dot`, `neato` or `fdp`.

```bash
$ dot euler.dot -Grankdir=BT -Tpng -o euler.png
```

You can pretty up your output using the XSL transform by [Vidar Hokstad](https://github.com/vidarh/diagram-tools):

```bash
$ dot euler.dot -Grankdir=BT -Tpng -o /tmp/euler.svg
$ xsltproc notugly.xsl /tmp/euler.svg > euler.svg
```

##Issues##

This program only finds direct ancestors by depth-first search and does not cover possible famous uncle advisors.
Parsing a webpage using regex is generally considered as bad habit by a lot of smart people. They are right. Suprisingly I still ignore them. Sorry for that.

And yes, the output looks awful.

##Thanks##

To the Mathematics Genealogy Project for their work, I hope very much to recieve a database dump someday. Given the already big number of request I hope this program doesn't overstrain their server load, otherwise automatic request distribution among the mirrors should be seriously considered from this site.

Jorge Cham for his comics, especially that one featuring [acedemic genealogy](http://www.phdcomics.com/comics.php?f=1419)
