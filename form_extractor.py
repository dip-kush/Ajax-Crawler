response=POST("url",payload,cookies)
soup=soup = BeautifulSoup(response.content,"html5lib")
tags = soup.findAll('input')
            for tag in tags:
                if tag.has_key('name'):
                    data[tag['name']] = ''
                    if tag.has_key('value') and tag['value']!="":
                        data[tag['name']] = tag['value']
                    else:
                        if tag.has_key('type'):
                             # This needs to be enhanced much more!
                             input_type = tag['type']
                             if input_type == "password":
                                 data[tag['name']] = STRING_GENERATOR.get_strong_password()
                             elif input_type == "email":
                                 data[tag['name']] = STRING_GENERATOR.get_email_address()
                             elif input_type == "url":
                                 data[tag['name']] = "http://" + STRING_GENERATOR.get_alpha_only_string() + ".com"
                             elif input_type =="submit":
                                data[tag['name']] =tag['value']
                             elif input_type =="file" :
                                files[tag['name']]=open(image, 'rb')

                             elif input_type == "hidden":
                                    #self.recent_string, data[tag['name']] = STRING_GENERATOR.get_tautology_string(QUOTE = QUOTE)
                                    if tag.has_key('value'):
                                        data[tag['name']] = tag['value']
                                    else:
                                        data[tag['name']] = STRING_GENERATOR.get_alpha_only_string()

                             else:
                                 data[tag['name']] = STRING_GENERATOR.get_alpha_only_string()

                elif tag.has_key('id'):
                    data[tag['id']] = ''
                    if tag.has_key('value') and tag['value']!="":
                       data[tag['id']] = tag['value']
                    else:
                        if tag.has_key('type'):
                            input_type = tag['type']
                            if input_type == "password":
                                data[tag['id']] = STRING_GENERATOR.get_strong_password()
                            elif input_type == "email":
                                data[tag['id']] = STRING_GENERATOR.get_email_address()
                            elif input_type == "url":
                                data[tag['id']] = "http://" + STRING_GENERATOR.get_alpha_only_string() + ".com"
                            elif input_type =="submit" :
                                data[tag['id']] =tag['value']
                            elif input_type =="file" :
                                files[tag['name']]=open(image, 'rb')
                            elif input_type == "hidden":
                                   #self.recent_string, data[tag['name']] = STRING_GENERATOR.get_tautology_string(QUOTE = QUOTE)
                                   if tag.has_key('value'):
                                       data[tag['id']] = tag['value']
                                   else:
                                       data[tag['id']] = STRING_GENERATOR.get_alpha_only_string()
                            else:
                                 data[tag['id']] = STRING_GENERATOR.get_alpha_only_string()



                else:
                    if tag.has_key('type'):
                        input_type = tag['type']
                        if tag.has_key('value'):
                           data[tag['value']]=tag['value']
                        if input_type =="submit" :
                            data[tag['type']] =tag['value']
                        else:
                            data[tag['type']] ="dummy data "





        if 'textareas' in self.consider_only:
            tags = soup.findAll('textarea')
            for tag in tags:
                if tag.has_key('name'):
                        data[tag['name']] = STRING_GENERATOR.get_alpha_only_string()
                else:
                        if tag.has_key('id'):
                                data[tag['id']] = STRING_GENERATOR.get_alpha_only_string()

        if 'selects' in self.consider_only:
            tags = soup.findAll('select')
            for tag in tags:
                if tag.has_key('name'):
                        #sel_name = tag['name']
                        data[tag['name']] = STRING_GENERATOR.get_alpha_only_string()
                else:
                        if tag.has_key('id'):
                                #sel_name = tag['name']
                                data[tag['id']] = STRING_GENERATOR.get_alpha_only_string()

        return data

