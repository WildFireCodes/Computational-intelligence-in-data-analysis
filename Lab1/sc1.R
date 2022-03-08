
#funkcja testowa
rosen <- function(x) {
  return( 100 * (x[2] - x[1] * x[1])^2 + (1 - x[1])^2 )
}


#narysujmy j¹ w zakresie od -2 do 2
x <- seq(-2,2,0.1)
y <- seq(-2,2,0.1)

n<-length(x)

xy<-expand.grid(x,y)

z<-rosen(xy)

zm<-matrix(as.matrix(z), ncol=n)

plot(x, y, type='n')
contour(x, y, zm, add=TRUE, lty=2,nlevels = 100)
#^na pewno mo¿na zrobiæ to ³adniej :) Jak? 

###pso bare bones###

#inicjalizacja
bx<-runif(16, min = -2, max = 2)
by<-runif(16, min = -2, max = 2)

b<-data.frame(bx,by)

#budujemy ramkê z pozycjami i wartoœci¹ funkcji celu
z<-as.numeric(as.matrix(rosen(b)))
b<-cbind(b,z)

#ustalamy który tak jest najlepszy
best_bird<-which.min(b$z)

#budujemy pust¹ ramkê na zapisanie evolucji rozwi¹zania 
best_evo<-data.frame(bx=double(),by=double(),z=double())

#to mo¿na zrobiæ ³adniej (i szybciej)
#ale na razie niech to bêdzie pêtla po interacjach
for (k in 1:100){ 

#pêtla po ptaszkach 
for (i in 1:16){

#odchylenia standardowe dla wymiaru x i y 
sigma_x<-abs(b$bx[i]-b$bx[best_bird])
sigma_y<-abs(b$by[i]-b$by[best_bird])

#testowe pozycje i wartoœæ funkcji 
test_x <- rnorm(1, mean=(b$bx[i]+b$bx[best_bird])/2 , sd=sigma_x)
test_y <- rnorm(1, mean=(b$by[i]+b$by[best_bird])/2 , sd=sigma_y)
test_z <- rosen(c(test_x,test_y))

#jeœli jestem lepszy ni¿ poprzedni robiê hop
if ( test_z < b$z[i] ) {
b$bx[i]<-test_x
b$by[i]<-test_y
b$z[i] <-test_z
}


} #ptaszki 

#który ptaszek jest teraz najlepszy?
best_bird<-which.min(b$z)

#zapis ewolucji rozwi¹zania
best_evo[k,]<-b[best_bird,]
} #iteracje 

#dorysowanie œcie¿ki znajdowania rozwi¹zania 
points(best_evo$bx,best_evo$by,t="b",pch=19)



