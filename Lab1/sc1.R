
#funkcja testowa
rosen <- function(x) {
  return( 100 * (x[2] - x[1] * x[1])^2 + (1 - x[1])^2 )
}


#narysujmy j� w zakresie od -2 do 2
x <- seq(-2,2,0.1)
y <- seq(-2,2,0.1)

n<-length(x)

xy<-expand.grid(x,y)

z<-rosen(xy)

zm<-matrix(as.matrix(z), ncol=n)

plot(x, y, type='n')
contour(x, y, zm, add=TRUE, lty=2,nlevels = 100)
#^na pewno mo�na zrobi� to �adniej :) Jak? 

###pso bare bones###

#inicjalizacja
bx<-runif(16, min = -2, max = 2)
by<-runif(16, min = -2, max = 2)

b<-data.frame(bx,by)

#budujemy ramk� z pozycjami i warto�ci� funkcji celu
z<-as.numeric(as.matrix(rosen(b)))
b<-cbind(b,z)

#ustalamy kt�ry tak jest najlepszy
best_bird<-which.min(b$z)

#budujemy pust� ramk� na zapisanie evolucji rozwi�zania 
best_evo<-data.frame(bx=double(),by=double(),z=double())

#to mo�na zrobi� �adniej (i szybciej)
#ale na razie niech to b�dzie p�tla po interacjach
for (k in 1:100){ 

#p�tla po ptaszkach 
for (i in 1:16){

#odchylenia standardowe dla wymiaru x i y 
sigma_x<-abs(b$bx[i]-b$bx[best_bird])
sigma_y<-abs(b$by[i]-b$by[best_bird])

#testowe pozycje i warto�� funkcji 
test_x <- rnorm(1, mean=(b$bx[i]+b$bx[best_bird])/2 , sd=sigma_x)
test_y <- rnorm(1, mean=(b$by[i]+b$by[best_bird])/2 , sd=sigma_y)
test_z <- rosen(c(test_x,test_y))

#je�li jestem lepszy ni� poprzedni robi� hop
if ( test_z < b$z[i] ) {
b$bx[i]<-test_x
b$by[i]<-test_y
b$z[i] <-test_z
}


} #ptaszki 

#kt�ry ptaszek jest teraz najlepszy?
best_bird<-which.min(b$z)

#zapis ewolucji rozwi�zania
best_evo[k,]<-b[best_bird,]
} #iteracje 

#dorysowanie �cie�ki znajdowania rozwi�zania 
points(best_evo$bx,best_evo$by,t="b",pch=19)



