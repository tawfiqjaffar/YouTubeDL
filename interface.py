from tkinter import *
from tkinter import ttk, StringVar, filedialog
from downloader import getVideos, DL


class Interface:
    def __init__(self, master):
        urlFrame = Frame(master)
        confFrame = Frame(master)
        thirdFrame = Frame(master)
        fourthFrame = Frame(master)
        self.urlLabel = Label(urlFrame, text="URL:")
        self.urlEntry = Entry(urlFrame, width=50)
        self.urlOkBtn = Button(urlFrame, text="OK", command=self._getVideos)

        self.videoComboLabel = Label(confFrame, text="Select Video Format:")
        self.videoComboDef = StringVar()
        self.videoCombo = ttk.Combobox(confFrame, width=50, postcommand=self.updateCombo)

        self.fileNameEntryLabel = Label(thirdFrame, text="Filename:")
        self.fileNameEntry = Entry(thirdFrame)
        self.destinationEntryLabel = Label(thirdFrame, text="Destination:")
        self.destinationEntry = Entry(thirdFrame)
        self.destinationBrowseBtn = Button(thirdFrame, text="Browse", command=self.browse)
        self.dest = ''
        self.confOkBtn = Button(thirdFrame, text="OK", command=self.goDL)

        self.console = Text(fourthFrame, width=100, height=10)

        urlFrame.pack(side=TOP)
        confFrame.pack(side=TOP)
        thirdFrame.pack(side=TOP)
        fourthFrame.pack()

        self.urlLabel.grid(row=0, column=0)
        self.urlEntry.grid(row=0, column=1,)
        self.urlOkBtn.grid(row=0, column=2)

        self.videoComboLabel.grid(column=0, row=0, sticky=E)
        self.videoCombo.grid(column=1, row=0)
        self.fileNameEntryLabel.grid(row=1, column=0)
        self.destinationEntry.grid(row=1, column=3)
        self.destinationEntryLabel.grid(row=1, column=2)
        self.fileNameEntry.grid(row=1, column=1)
        self.destinationBrowseBtn.grid(row=1, column=4)
        self.confOkBtn.grid(row=1, column=5)
        self.console.pack()

    def browse(self):
        self.dest = filedialog.askdirectory() + '/'
        self.destinationEntry.insert(0, self.dest)
        self.console.insert(END, "Selected destination directory: " + self.dest + '\n')

    def _getVideos(self):
        # print(getVideos(self.urlEntry.get()))
        self.console.insert(END, "Fetching YouTube video...\n")
        vid = getVideos(self.urlEntry.get())
        self.updateCombo(vid[0])
        self.console.insert(END, "Got video!\n\tFile name: {}\n".format(vid[1]))

    def updateCombo(self, values):
        self.videoCombo['values'] = values
        self.videoCombo.current(0)

    def goDL(self):
        ext = ''
        res = ''
        self.console.insert(END, "DOWNLOADING...\n\n")
        if 'mp4' in self.videoCombo.get():
            ext = 'mp4'
        if '720p' in self.videoCombo.get():
            res = '720p'
        DL(self.fileNameEntry.get(), self.dest, ext, res)
        self.console.insert(END, "DOWNLOADED!\n")
