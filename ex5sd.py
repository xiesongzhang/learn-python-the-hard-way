name='zed A. shaw'
age=35 #not a lie 
height=74#inches
weight=180#lbs
eyes='blue'
teeth='white'
hair='brown'

print "let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (eyes,hair)
print "His teeth are usually %s depending on the coffe."% teeth

print "%r  %r  %r" % (name,age,eyes)


# this line is tricky,try to get it exactly right
print "if i add %d, %d,and %d i get %d."% (age,height,weight,age + height+weight)

print"He's %d tall,%d heavy." % (height*2.54,weight*0.4535924)
