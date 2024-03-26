import app.io.input as im
import app.io.output as om

def main():
    if True:
        res = im.read_prompt()
        om.puts(res)
        om.write_to_file('./out/output.txt', res)

    if True:
        res = im.read_file_builtin("./data/foo.txt")
        om.puts(res)
        om.write_to_file('./out/output_builtin.txt', res)

    if True:
        res = im.read_file_pandas("./data/foo.txt")
        om.puts(res)
        om.write_to_file('./out/output_pandas.txt', res)
    # if True:
    #     res = im.read_prompt()
    #     om.puts(res)


if __name__ == "__main__":
    main()


