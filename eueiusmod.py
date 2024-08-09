# Assuming query and reply_markup are defined earlier in the code
async def edit_message(query, reply_markup):
    await query.edit_message_text(text='Please choose:', reply_markup=reply_markup)

# Calling the edit_message function
await edit_message(query, reply_markup)
