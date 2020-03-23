#package resources
#https://www.rdocumentation.org/
#https://rdrr.io/

#training
#https://rstudio.com/resources/training/

#logical operators
https://stat.ethz.ch/R-manual/R-devel/library/base/html/Logic.html
! x
x & y
x && y
x | y
x || y
xor(x, y)

isTRUE (x)
isFALSE(x)
is.null(x)

#distinct rows
distinct()  #dplyr 
unique()

#explore data
mtcars[order(mpg, -cyl),]

#cleaning
d$a <- factor(d$a)


#shiny
#training
#https://shiny.rstudio.com/tutorial/

#https://www.rdocumentation.org/packages/shinyWidgets/versions/0.5.0/topics/updatePickerInput
#http://shinyapps.dreamrs.fr/shinyWidgets/

#layout
#https://shiny.rstudio.com/articles/layout-guide.html

#widget
##shinyWidget
##https://dreamrs.github.io/shinyWidgets/
prettyCheckbox()
searchInput()

##html
#https://shiny.rstudio.com/articles/tag-glossary.html
#https://shiny.rstudio.com/tutorial/written-tutorial/lesson2/
#
##app great example
##https://shiny.rstudio.com/gallery/animal-tracking.html
