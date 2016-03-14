from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(open("split.pdf", "rb"))
input2 = PdfFileReader(open("split.pdf", "rb"))
# print how many pages input1 has:
print "document1.pdf has %d pages." % input1.getNumPages()



for i in range (input1.getNumPages()):
	page5 = input1.getPage(i)
	page6 = input2.getPage(i)
	page5.mediaBox.upperRight = (
    	page5.mediaBox.getUpperRight_x() / 2,
    	page5.mediaBox.getUpperRight_y()
	)
	output.addPage(page5)
	
	page6.mediaBox.upperLeft = (
    	page6.mediaBox.getUpperRight_x()/2,
    	page6.mediaBox.getUpperLeft_y()
	)
	output.addPage(page6)




# add some Javascript to launch the print window on opening this PDF.
# the password dialog may prevent the print dialog from being shown,
# comment the the encription lines, if that's the case, to try this out
output.addJS("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")

# encrypt your new PDF and add a password
#password = "secret"
#output.encrypt(password)

# finally, write "output" to document-output.pdf
outputStream = file("split-output.pdf", "wb")
output.write(outputStream)
