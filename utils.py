def is_author_in_channel(ctx):
    if ctx.author.voice is None:
        return True
    return False

