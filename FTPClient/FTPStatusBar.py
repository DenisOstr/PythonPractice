import wx

class FtpStatusBar(wx.StatusBar):
	def __init__(self, parent):
		wx.StatusBar.__init__(self, parent)
		
		self.SetFieldsCount(2)
		self.SetStatusText('Welcome to Ftp Client', 0)
		self.SetStatusWidths([-5, -2])
		self.icon = wx.StaticBitmap(self, -1, wx.Bitmap('image/disconnect.png'))
		self.Bind(wx.EVT_SIZE, self.OnSize)
		self.PlaceIcon()
		
	
	def PlaceIcon(self):
		rect = self.GetFieldRect(1)
		self.icon.SetPosition((rect.x + 3, rect.y + 3))
		
		
	def OnSize(self, event):
		self.PlaceIcon()