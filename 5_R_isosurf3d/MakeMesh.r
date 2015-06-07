require(akima) ; require(rgl) ; require(scatterplot3d) ; require(animation) ; require(plot3D)
fpe = read.table("/Users/aolejniczak/Desktop/Points.txt", col.names=c("xcol","ycol","zcol"))
x <- as.vector(fpe$xcol)
y <- as.vector(fpe$ycol)
z <- as.vector(fpe$zcol)
xyz <- mesh(x, y, z)
F <- with(xyz, log(x^2 + y^2 + z^2 + 10*(x^2 + y^2) * (y^2 + z^2) ^2))
# use shading for level = 1 - show triangulation with border
isosurf3D(x, y, z, F, level = 48.4, shade = 0.9,
           col = "yellow", border = "orange")

#cat("Creating the array.")
#v <- array(0 , dim = c( length( x ) , length( y ) , length( z ) ) )

#cat("The size of v is: ",length(v))

#cat("Seeding the array with dummy values (1,1,1).")
#v[ , , ] <- 1:1:1

#cat("Now making the isosurface.")
#isosurf3D(x,y,z, colvar=v,phi = 40, theta = 40,
#         level = mean(v, na.rm = TRUE), isofunc = createisosurf,
#        col = NULL, border = NA, facets = TRUE,
#         colkey = NULL, panel.first = NULL,
#         clab = NULL, bty = "b",
#         lighting = FALSE, shade = 0.5, ltheta = -135, lphi = 0,
#         add = FALSE, plot = TRUE)

#s=interp(x,y,z, duplicate="..")
#cat(dim(s$z))
#zlim <- range(z)
#zlen <- zlim[2] - zlim[1] + 1
#colorlut <- terrain.colors(zlen,alpha=0) # height color lookup table
#col <- colorlut[ z-zlim[1]+1 ] # assign colors to heights for each point
#surface3d(s$x,s$y,s$z, color=col, alpha=0.75, back="lines")