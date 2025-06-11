import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from screens.principal import root
from screens import register
from screens import login

root.mainloop()