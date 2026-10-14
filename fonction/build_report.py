import fabric.functions as fn

udf = fn.UserDataFunctions()

@udf.function()
def build_report(fileName: str, rowsRead: int) -> str:
    stamp = fileName.split("_")[-1].replace(".csv", "")
    if len(stamp) == 4 and stamp.isdigit():
        wave = stamp[0:2] + " h " + stamp[2:4]
    else:
        wave = stamp
    if rowsRead >= 115:
        load = "vague lourde"
    else:
        load = "vague normale"
    return "Quai de Metz, vague de " + wave + " : " + str(rowsRead) + " colis fusionnés dans shipments (" + load + ")."
