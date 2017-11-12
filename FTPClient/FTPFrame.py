from ftplib import FTP, all_errors
import wx
import FTPStatusBar

class FtpFrame(wx.Frame, FTPStatusBar.FtpStatusBar):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, size = (250, 270))
		
		wx.StaticText(self, -1, 'Ftp site', (10, 20))
		wx.StaticText(self, -1, 'Login', (10, 60))
		wx.StaticText(self, -1, 'Password', (10, 100))
		
		self.ftpsite = wx.TextCtrl(self, -1, '', (110, 15), (120, -1))
		self.login = wx.TextCtrl(self, -1, '', (110, 55), (120, -1))
		self.password = wx.TextCtrl(self, -1, '', (110, 95), (120, -1), style = wx.TE_PASSWORD)
		
		self.ftp = None
		
		connect = wx.Button(self, 1, 'Connect', (10, 160))
		disconnect = wx.Button(self, 2, 'Disconnect', (120, 160))
		
		self.Bind(wx.EVT_BUTTON, self.OnConnect, id = 1)
		self.Bind(wx.EVT_BUTTON, self.OnDisconnect, id = 2)
		
		self.statusbar = FTPStatusBar.FtpStatusBar(self)
		self.SetStatusBar(self.statusbar)
		self.Centre()
		
	
	def OnConnect(self, event):
		if not self.ftp:
			ftpsite = self.ftpsite.GetValue()
			login = self.login.GetValue()
			password = self.password.GetValue()
			
			try:
				self.ftp = FTP(ftpsite)
				LogIn = self.ftp.login(login, password)
				self.statusbar.SetStatusText('User connected')
				self.statusbar.icon.SetBitmap(wx.Bitmap('image/connect.png'))
				
			except AttributeError:
				self.statusbar.SetForegroundColour(wx.RED)
				self.statusbar.SetStatusText('Incorrect params')
				self.ftp = None
				
			except (all_errors, error):
				self.statusbar.SetStatusText(str(error))
				self.ftp = None
		
		
	def OnDisconnect(self, event):
		if self.ftp:
			self.ftp.quit()
			self.ftp = None
			self.statusbar.SetStatusText('User Disconnected')
			self.statusbar.icon.SetBitmap(wx.Bitmap('image/disconnect.png'))