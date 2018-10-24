import markovify
import csv
import pandas

#import lyrics
# with open('songdata.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         line_count += 1
#     print(f'Processed {line_count} lines.')

# lyrics = pandas.read_csv('songdata.csv')
# abba = lyrics.loc[lyrics['artist'] == 'ABBA'].drop(columns=['artist', 'song', 'link'])
# roxette = lyrics.loc[lyrics['artist'] == 'Roxette'].drop(columns=['artist', 'song', 'link'])
# #export to txt
# abba.to_csv('./data/abba.txt', header=None, index=None, sep=' ', mode='a')
# roxette.to_csv('./data/roxette.txt', header=None, index=None, sep=' ', mode='a')

#import the models from the txt files
abba = open("./data/abba.txt").read()
roxette = open("./data/roxette.txt").read()

#create the models via markovify
text_model0 = markovify.Text(abba, state_size=1)
text_model1 = markovify.Text(roxette, state_size=1)

#create a combination of the models. I am currently ommitting the shakespeare model
model_combo = markovify.combine([ text_model0, text_model1 ], [ 1, 1])

poem = ""
#generate 4 lines of text based off the model that was created
for i in range(8):
	poem = poem + model_combo.make_short_sentence(70)
	if i < 7:
		poem += '\n'
print(poem)

#write the generated text to file 'output.txt'
text_file = open("output.txt", "w")
text_file.write(poem)
text_file.close()

