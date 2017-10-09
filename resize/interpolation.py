class interpolation:

    def linear_interpolation(self, pt1, pt2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        #Write your code for linear interpolation here
        #pt1 (leftx,pix)
        #pt2 (rightx,pix)
        #unknown = dx

        if(pt1[0] != pt2[0]):
            fpart = pt1[1] * ((pt2[0] - unknown) / (pt2[0] - pt1[0]))
            spart = pt2[1] * ((unknown - pt1[0]) / (pt2[0] - pt1[0]))
            pix = fpart + spart
        else:
            pix = pt1[1]

        return pix

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolatio method to compute this task

        #pt1(leftx, q11, q12)
        #pt2(rightx, q21, q22)
        #pt3(bottomy)
        #pt4(topy)

        if (pt2[0] - pt1[0]) != 0:
            r1 = self.linear_interpolation((pt1[0],pt1[1]),(pt2[0],pt2[1]),unknown[0])
            r2 = self.linear_interpolation((pt1[0],pt1[2]),(pt2[0],pt2[2]), unknown[0])
        else:
            r1 = pt1[1]
            r2 = pt1[2]

        if (pt3 - pt4) != 0:
            avgPix = self.linear_interpolation((pt4,r2), (pt3,r1), unknown[1])
        else:
            avgPix = (int(pt1[1]) + int(pt1[2]) + int(pt2[1]) + int(pt2[2]))/4

        return avgPix
