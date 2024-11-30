import json
import os
import hashlib

blockchain_dir='blockchain/'

def hashGenerator(prev_block):
	with open(blockchain_dir+prev_block,'rb')as f:
		content=f.read()
	return hashlib.md5(content).hexdigest()

def create_genesis_block():
    if not os.path.exists(blockchain_dir):
        os.makedirs(blockchain_dir)

    if not os.path.exists(blockchain_dir + '0'):
        data = {
            "holder": "None",
            "amount": 0,
            "type": "Genesis",
            "prev_block": {
                "hash": None,
                "filename": None
            }
        }
        with open(blockchain_dir + '0', "w", newline="\n") as f:
            json.dump(data, f, indent=4)

def check_integrity():
	#convert filenames to int data type using lambda x 
	files=sorted(os.listdir(blockchain_dir),key=lambda x:int(x))
	print(files)
	results=[]
	#read hash of all previous block except first block
	for file in files [1:]:
		#read the file and pass it to json load function
		with open(blockchain_dir+file)as f:
			block=json.load(f)#dictionary type

		prev_hash=block.get('prev_block').get('hash')
		prev_file=block.get('prev_block').get('filename')
		print(prev_hash)
		#compare the hash written in the block with actual hash of previous block
		actual_hash=hashGenerator(prev_file)
		if prev_hash==actual_hash:
			res='ok'
		else:
			res='was changed'
		print(f"block {prev_file} :{res}")
		results.append({'block':prev_file,'results':res})
	return results
	
def write_block(holder,amount,type):
	# call hashGenerator and pass the name of the prev block 
	#since we are using integers for the name of file we can use the length of the files list to determine the filename of prev block
	blocks_count=len(sorted(os.listdir(blockchain_dir),key=lambda x:int(x)))
	prev_block=str(blocks_count)

	data={
	"holder":holder,
	"amount":amount,
	"type":type,
	"prev_block":{
	"hash":hashGenerator(prev_block) if blocks_count > 0 else None,"filename":prev_block
	}
	} 
	current_block=blockchain_dir+str(blocks_count+1)
	json_object= json.dumps(data, indent=4)
 	#write the data into file as json object 
 	#newline as in unix systems file should end in newline
	with open(current_block, "w") as f:
		f.write(json_object)
		f.write('\n')
            
    	
def main():
	#write_block('kaviya',1000,"withdraw")
	create_genesis_block()
	check_integrity()

if __name__ == '__main__':
    main()
