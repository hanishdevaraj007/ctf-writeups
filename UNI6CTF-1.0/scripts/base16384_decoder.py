import pybase16384

# Encoded challenge payload
encoded_text = """
𐙉𓈠驨𓄠陨𒁤𓅷𒀠啦鵴啥驮𔕴𓁯慫阠頠𖥲𓉰啯陨ꉣ𓁥餠顥饯饥騠顮𖥲𓉰饥頠陨𐙩慳𓈠陲鹣鱮鴠饩驤啮𓁴𐙡陳𓉣𒁩𓅮阠𓁣𓅯啳鵴啥ꍢ顯顫陨𐙩䄮稊驶𖥲ꈠ𖥥𓌠ꍮ顯驫啤啡驳𓁣𓉥唬𓁰𔑯𐙩啧鵴𓉡鸠啮鵴啥𒁷ꍲ啤魯頠𖥲𓉰慯𐘠𓉯鹨鱮鸠啳𓁴ꍵ啹𐙩鹶鹳ꍢ𦡥𡪀𐙯𖥬鴠𓁡驤啲𒁴鬠𐙩捤㸍㸍䄉𓌊鹮𠄶敃鱮畲𓍴界敩𓅮絟楀驫鑲教鑵敆𐙵鑤鵴鑥𓁲楥鑴畂驳樶栵鐶腆鱀ᕽ
"""

# Base16384 libraries expect UTF-16BE byte formatting
raw_bytes = encoded_text.encode("utf-16be")

# Decode the payload
decoded_bytes = pybase16384.decode(raw_bytes)

try:
    # Attempt UTF-8 decoding
    output = decoded_bytes.decode("utf-8")

    print("[+] Decoded Text:")
    print(output)

except UnicodeDecodeError:
    # Save binary output if not plaintext
    print("[!] Binary data detected.")
    print("[+] Saving output as artifact.bin")

    with open("artifact.bin", "wb") as file:
        file.write(decoded_bytes)