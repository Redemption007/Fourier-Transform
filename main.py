from setters import set_glob
from variables import window, h, w

window.title("Signal Analyse")
window.geometry("{}x{}".format(w, h))

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

set_glob(window)

window.mainloop()