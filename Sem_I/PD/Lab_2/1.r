A<-data.frame(Ident=c(1,2,3,4,5), sexe=c("H","F","F","H","H"), Poids=c(75,68,48,72,83))
B<-data.frame(Ident=c(1,2,3,4,5), sexe=c("H","F","F","H","H"), Taille=c(182,165,160,178,183))
print(A)
print(B)
C<-merge(A,B, by = c("Ident","sexe"), all=TRUE)
print(C)
