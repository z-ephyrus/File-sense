import os
import fleep

#print("here")

def scanfile(path):
    try:
        with open(path, "rb") as f:
            content = f.read(128)
        info = fleep.get(content)

        return {
            "file": path,
            "type": info.type,
            "extension": info.extension,
            "mime": info.mime,
        }
    except Exception as e:
        return {"file":path ,"error": str(e)}


def scandirectory(directory):
    results = []
    for root, _, files in os.walk(directory):
        for f in files:
            fp = os.path.join(root, f)
            results.append(scanfile(fp))
    return results
