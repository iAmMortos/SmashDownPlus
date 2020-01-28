
class Characters(object):

  def __init__(self, file='characters.txt'):
    self._chars = {}
    self._excluded = {}
    with open(file) as f:
      lines = [line.strip() for line in f.readlines()]
      for line in lines:
        if not line.startswith('#'):
          num, char = line.split('\t')
          self._chars[num] = char
        else:
          exline = line[1:].strip()
          num, char = exline.split('\t')
          self._excluded[num] = char

  def list_alpha(self):
    return sorted(list(self._chars.values()))

  def list_roster(self):
    return [pair[1] for pair in sorted(list(self._chars.items()), key=lambda a: a[0])]

  def __len__(self):
    return len(self._chars)


if __name__ == '__main__':
  c = Characters()
  print(c.list_roster())
