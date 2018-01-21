savefile = open("new.txt",'w')
for x in range(48,122):
    savefile.write(chr(x)+'\n')
    for y in range(48,122):
        savefile.write(chr(x)+chr(y)+'\n')
        for z in range(48,122):
            savefile.write(chr(x)+chr(y)+chr(z)+'\n')
            for a in range(48,122):
                savefile.write(chr(x)+chr(y)+chr(z)+chr(a)+'\n')
                for b in range(48,122):
                    savefile.write(chr(x)+chr(y)+chr(z)+chr(a)+chr(b)+'\n')
                    for c in range(48,122):
                        savefile.write(chr(x)+chr(y)+chr(z)+chr(a)+chr(b)+chr(c)+'\n')
                        for d in range(48,122):
                            savefile.write(chr(x)+chr(y)+chr(z)+chr(a)+chr(b)+chr(c)+chr(d)+'\n')
                            for e in range(48,122):
                                savefile.write(chr(x)+chr(y)+chr(z)+chr(a)+chr(b)+chr(c)+chr(d)+chr(e)+'\n')
                                for f in range(48,122):
                                    savefile.write(chr(x)+chr(y)+chr(z)+chr(a)+chr(b)+chr(c)+chr(d)+chr(e)+chr(f)+'\n')
                                    for g in range(48,122):
                                        savefile.write(chr(x)+chr(y)+chr(z)+chr(a)+chr(b)+chr(c)+chr(d)+chr(e)+chr(f)+chr(g)+'\n')
                                        for h in range(48,122):
                                            savefile.write(chr(x)+chr(y)+chr(z)+chr(a)+chr(b)+chr(c)+chr(d)+chr(e)+chr(f)+chr(g)+chr(h)+'\n')
        
savefile.close