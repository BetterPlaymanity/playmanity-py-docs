import playmanity

clientinit = playmanity.accounts.Bot("X","x")
callback = clientinit.run()
client = callback

print(playmanity.get.getBotProfile(client))
print(playmanity.get.getProfile(5))