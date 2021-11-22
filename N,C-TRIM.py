{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bd67e05a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Save sequences in text file, line after another not as fasta. \n",
    "#Program to read  N amino acids from N terminal\n",
    "# from each line in python \n",
    "\n",
    "import time\n",
    "\n",
    "# Opening the file\n",
    "File = open('file name.txt','r')\n",
    "\n",
    "while(True):\n",
    "    # Reading line using readline()\n",
    "    data = File.readline()\n",
    "    if(data==''):break\n",
    "    #  Printing 10 character from each line \n",
    "    print(data[0:N],end=' ')#N = number of residues. \n",
    "    time.sleep(0.3)\n",
    "\n",
    "File.close()\n",
    "\n",
    "\n",
    "#Program to read  N amino acids from C terminal\n",
    "# from each line in python \n",
    "import time\n",
    "\n",
    "# Opening the file\n",
    "File = open('file name.txt','r')\n",
    "\n",
    "while(True):\n",
    "    # Reading line using readline()\n",
    "    data = File.readline()\n",
    "    if(data==''):break\n",
    "    print(data[-N:],end=' ')#N = number of residues. \n",
    "    time.sleep(0.3)\n",
    "\n",
    "File.close()    \n",
    "\n",
    "#reverese the string direction to get C terminal residues \n",
    "# Python code to reverse a string \n",
    "# using loop\n",
    "  \n",
    "def reverse(s):\n",
    "  str = \"\"\n",
    "  for i in s:\n",
    "    str = i + str\n",
    "  return str"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
