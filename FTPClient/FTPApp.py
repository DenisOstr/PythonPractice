import wx
import FTPStatusBar
import FTPFrame

class FtpApp(wx.App):
	def OnInit(self):
		frame = FTPFrame.FtpFrame(None, -1, 'Ftp Client')
		frame.Show(True)
		return True
		
app = FtpApp(0)
app.MainLoop()