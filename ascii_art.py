fox_main = """
  ██▓▓                                                                              
██▓▓▓▓▓▓▓▓                                    ████████████                          
██▓▓▓▓▓▓▓▓████                            ████▓▓▓▓▓▓▓▓▓▓██                          
██▓▓████▓▓▓▓▓▓██                        ██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓                        
██▓▓██▒▒██▓▓▓▓▓▓████    ████████      ██▓▓▓▓▓▓▓▓████▒▒██▓▓▓▓                        
██▓▓██▒▒▒▒██▓▓▓▓▓▓▓▓████░░░░░░░░██████░░░░▓▓▓▓██▒▒▒▒▒▒██▓▓▓▓                        
██▓▓██▒▒▒▒▒▒████░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒▒▒▒▒▓▓▓▓▓▓▓▓                        
██▓▓██▒▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒▒▒▒▒▒▒▒▒██▓▓▓▓                          
██▓▓██▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒▒▒▒▒██▓▓██                          
██▓▓▓▓██▒▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒██░░░░██                          
  ██░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░██                          
  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██        ██▓▓                
  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓          ██  ▓▓              
    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓        ██    ▓▓            
    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓        ██      ▓▓          
    ██░░░░░░██████░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░▓▓        ██        ▓▓        
    ██░░░░░░██████░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░██      ██          ▓▓      
    ██░░░░░░████  ░░░░░░░░░░░░░░░░░░████  ░░░░░░░░░░░░░░▓▓      ██          ▓▓      
  ▓▓░░░░░░░░████▓▓░░░░░░░░░░░░░░░░░░████▓▓░░░░░░░░░░░░░░░░██    ██            ▓▓    
  ▓▓░░░░░░░░██████░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░██    ██            ██    
▒▒░░░░░░░░░░░░▒▒░░      ▒▒▓▓      ░░░░░░░░░░░░░░░░░░░░░░░░██    ██              ██  
▓▓░░░░░░░░░░            ░░░░          ░░░░░░░░░░░░░░░░░░░░    ░░░░              ██  
  ██░░░░                                        ░░░░░░████  ██                    ██
    ██                ██    ██                    ░░██      ██░░░░░░      ░░      ██
      ▓▓                ████                    ████      ██░░░░░░░░  ░░░░░░      ██
        ▓▓                                  ████        ▓▓░░░░░░░░░░░░░░░░░░  ░░░░██
          ░░▒▒                        ▓▓▓▓▓▓██████▒▒    ██░░░░░░░░░░░░░░░░░░░░░░░░██
              ██████              ░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░██
                  ██            ░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░██
                  ██            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░▓▓██
                  ██            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░▓▓  
                  ██░░          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░▓▓    
                  ██░░            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░░░▓▓    
                  ██░░              ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░▓▓      
                  ▓▓░░░░            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██▓▓        
                  ▓▓░░░░░░          ░░░░░░░░░░░░░░      ░░░░░░░░░░▓▓████            
                ██░░░░░░░░          ░░░░░░░░░░░░██        ░░░░░░░░▓▓                
                ▓▓░░░░░░░░░░██      ░░░░░░░░░░░░██      ░░░░░░░░░░▓▓                
                ▓▓░░▓▓▓▓░░░░░░██████░░░░░░▓▓░░░░████████░░░░░░░░░░▓▓                
                ▓▓▓▓▓▓▓▓▓▓░░▒▒    ██▓▓░░▓▓▓▓▓▓░░██░░░░██░░▓▓▓▓▓▓░░▓▓                
              ░░▓▓▓▓▓▓▓▓▓▓▒▒██      ▓▓▒▒▓▓▓▓▓▓▒▒██▓▓▒▒██▒▒▓▓▓▓▓▓▒▒▓▓                
              ██▓▓▓▓▓▓▓▓▓▓██        ▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██                
              ██▓▓▓▓▓▓▓▓▓▓██        ██▓▓▓▓▓▓▓▓▓▓██▓▓████▓▓▓▓▓▓▓▓██                  
              ██▓▓▓▓▓▓▓▓▓▓██        ██▓▓▓▓▓▓▓▓▓▓████  ██▓▓▓▓▓▓▓▓██                  
                ██████████            ██████████        ████████                    
"""

