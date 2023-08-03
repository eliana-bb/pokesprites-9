import requests
import json

refs = [
	"File:Menu HOME 0907.png",
	"File:Menu HOME 0908.png",
	"File:Menu HOME 0909.png",
	"File:Menu HOME 0910.png",
	"File:Menu HOME 0911.png",
	"File:Menu HOME 0912.png",
	"File:Menu HOME 0913.png",
	"File:Menu HOME 0914.png",
	"File:Menu HOME 0915.png",
	"File:Menu HOME 0916.png",
	"File:Menu HOME 0916-Female.png",
	"File:Menu HOME 0917.png",
	"File:Menu HOME 0918.png",
	"File:Menu HOME 0919.png",
	"File:Menu HOME 0920.png",
	"File:Menu HOME 0921.png",
	"File:Menu HOME 0922.png",
	"File:Menu HOME 0923.png",
	"File:Menu HOME 0924.png",
	"File:Menu HOME 0925.png",
	"File:Menu HOME 0925-Three.png",
	"File:Menu HOME 0926.png",
	"File:Menu HOME 0927.png",
	"File:Menu HOME 0928.png",
	"File:Menu HOME 0929.png",
	"File:Menu HOME 0930.png",
	"File:Menu HOME 0931.png",
	"File:Menu HOME 0931-Blue.png",
	"File:Menu HOME 0931-White.png",
	"File:Menu HOME 0931-Yellow.png",
	"File:Menu HOME 0932.png",
	"File:Menu HOME 0933.png",
	"File:Menu HOME 0934.png",
	"File:Menu HOME 0935.png",
	"File:Menu HOME 0936.png",
	"File:Menu HOME 0937.png",
	"File:Menu HOME 0938.png",
	"File:Menu HOME 0939.png",
	"File:Menu HOME 0940.png",
	"File:Menu HOME 0941.png",
	"File:Menu HOME 0942.png",
	"File:Menu HOME 0943.png",
	"File:Menu HOME 0944.png",
	"File:Menu HOME 0945.png",
	"File:Menu HOME 0946.png",
	"File:Menu HOME 0947.png",
	"File:Menu HOME 0948.png",
	"File:Menu HOME 0949.png",
	"File:Menu HOME 0950.png",
	"File:Menu HOME 0951.png",
	"File:Menu HOME 0952.png",
	"File:Menu HOME 0953.png",
	"File:Menu HOME 0954.png",
	"File:Menu HOME 0955.png",
	"File:Menu HOME 0956.png",
	"File:Menu HOME 0957.png",
	"File:Menu HOME 0958.png",
	"File:Menu HOME 0959.png",
	"File:Menu HOME 0960.png",
	"File:Menu HOME 0961.png",
	"File:Menu HOME 0962.png",
	"File:Menu HOME 0963.png",
	"File:Menu HOME 0964.png",
	"File:Menu HOME 0964-Hero.png",
	"File:Menu HOME 0965.png",
	"File:Menu HOME 0966.png",
	"File:Menu HOME 0967.png",
	"File:Menu HOME 0968.png",
	"File:Menu HOME 0969.png",
	"File:Menu HOME 0970.png",
	"File:Menu HOME 0971.png",
	"File:Menu HOME 0972.png",
	"File:Menu HOME 0973.png",
	"File:Menu HOME 0974.png",
	"File:Menu HOME 0975.png",
	"File:Menu HOME 0976.png",
	"File:Menu HOME 0977.png",
	"File:Menu HOME 0978.png",
	"File:Menu HOME 0978-Droopy.png",
	"File:Menu HOME 0978-Stretchy.png",
	"File:Menu HOME 0979.png",
	"File:Menu HOME 0980.png",
	"File:Menu HOME 0981.png",
	"File:Menu HOME 0982.png",
	"File:Menu HOME 0983.png",
	"File:Menu HOME 0984.png",
	"File:Menu HOME 0985.png",
	"File:Menu HOME 0986.png",
	"File:Menu HOME 0987.png",
	"File:Menu HOME 0988.png",
	"File:Menu HOME 0989.png",
	"File:Menu HOME 0990.png",
	"File:Menu HOME 0991.png",
	"File:Menu HOME 0992.png",
	"File:Menu HOME 0993.png",
	"File:Menu HOME 0994.png",
	"File:Menu HOME 0995.png",
	"File:Menu HOME 0996.png",
	"File:Menu HOME 0997.png",
	"File:Menu HOME 0998.png",
	"File:Menu HOME 0999.png",
	"File:Menu HOME 0999-Roaming.png",
	"File:Menu HOME 1000.png",
	"File:Menu HOME 1001.png",
	"File:Menu HOME 1002.png",
	"File:Menu HOME 1003.png",
	"File:Menu HOME 1004.png",
	"File:Menu HOME 1005.png",
	"File:Menu HOME 1006.png",
	"File:Menu HOME 1007.png",
	"File:Menu HOME 1007-Sprinting.png",
	"File:Menu HOME 1008.png",
	"File:Menu HOME 1008-Drive.png",
	"File:Menu HOME 1009.png",
	"File:Menu HOME 1010.png"
]
for ref in refs:
	sc = 0
	content = ""
	while sc != 200:
		req = requests.get(f"https://archives.bulbagarden.net/wiki/{ref.replace(' ', '_')}")
		sc = req.status_code
		content = str(req.content)
	source_ref_start = content.find("content=\"https://archives.bulbagarden.net/media/upload") + 9
	source_ref_end = content.find(".png", source_ref_start) + 4
	source_ref = content[source_ref_start:source_ref_end]

	species_num = int(source_ref[61:65])
	species_suffix = source_ref[65:-4]
	sc = 0
	while sc != 200:
		req = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{species_num}")
		sc = req.status_code
		content = req.content
	pokeapi_response = json.loads(content)
	species_name = pokeapi_response['names'][6]['name']

	sc = 0
	while sc != 200:
		req = requests.get(source_ref)
		sc = req.status_code
		content = req.content

	with open(f"ims/{species_name}{species_suffix}.png".lower().replace(" ", "-"), "wb+") as outfile:
		outfile.write(content)

	print(f"{species_name}{species_suffix}")