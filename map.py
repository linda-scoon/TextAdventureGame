### MAP OF THE GAME WORLD #####
world_map = {'Recycle Plant': {'VIEW': 'The Recycle Plant is bustling with activity as recycle bots dissemble other robots and sort their components into various recycling units.\nCareful don’t get too close least you be recycled.',
                               'NE': 'Welcome Bridge',
                               'N': 'Train Station',
                               'E': 'City Gates',
                               'GROUND': {'bionic arm ': {'Info': 'Rusty and Stiff, in great need of oiling, but very light',
                                                          'Takeable': True,
                                                          'Recollectable': False}}},
             'City Gates': {'VIEW': 'The City gates that once used to be glamorous have rusted away, leaving a frame that dissipates into dust from a touch.\n',
                            'N': 'Welcome Bridge',
                            'S': 'Droid Forest',
                            'W': 'Recycle Plant',
                            'GROUND': {'stones': {'Info': 'Cold to the touch, filled with thick moss',
                                                  'Takeable': False,
                                                  'Recollectable': False}}},
             'Algor Apartments': {'VIEW': 'A tree is growing out of the reception, some floors caved in, and the entire building has no glass on its windows due to a fire that blew them all out.\n',
                                  'NW': 'Droid Factory',
                                  'NE': 'Shopping Centre',
                                  'SE': 'City Centre',
                                  'SW': 'Train Station',
                                  'GROUND': {'a comb ': {'Info': 'brown with a black handle, dirty but in perfect condition',
                                                         'Takeable': True,
                                                         'Recollectable': False}}},
             'Droid Factory': {'VIEW': 'The most well-maintained building. There’s a bustle of busy bots.\nWorking hard doing what they were programmed to do.',
                               'N': 'Wind Turbines',
                               'SE': 'Algor Apartments',
                               'S': 'Train Station',
                               'GROUND': {'lab coat ': {'Info': 'It\'s a creamy white, most of it has been eaten by moths',
                                                        'Takeable': True,
                                                        'Recollectable': False},
                                          'a pen ': {'Info': 'Ink is dry, but it looks as good as new',
                                                     'Takeable': True,
                                                     'Recollectable': False}}},
             'Droid Forest': {'VIEW': 'This forest is filled with dangerous malfunctioning robots that escaped the Recycle Plant. The forest is forever dark, even on the sunniest days.\nDistant sounds of birds chirping can be heard, but the beautiful sound is interrupted by the unnatural sound of metal, squeaking, clanging....',
                              'N': 'City Gates',
                              'GROUND': {'trees': {'Info': 'thick bark that can be peeled off, beautiful long branches, dark green leaves, too high to reach',
                                                   'Takeable': False,
                                                   'Recollectable': False},
                                         'bark ': {'Info': 'smells woody',
                                                   'Takeable': True,
                                                   'Recollectable': True}},
                              },
             'Power Station': {'VIEW': 'Barb wired fence with warning signs all over.\nRestricted access only approved bots may enter.',
                                       'NW': 'Google Bridge',
                                       'W': 'Welcome Bridge',
                                       'E': 'WaterFall',
                                       'GROUND': {'warning Signs': {'Info': 'White plastic. All the writing has been washed off',
                                                                    'Takeable': True,
                                                                    'Recollectable': False}}},
             'City Centre': {'VIEW': 'The remnants of a bar stands to your right. What is left of a clinic right ahead of you and numerous other unrecognisable buildings.\nThe roof of a building caves in as you take in the site. It’s not safe to enter any of them.',
                             'N': 'Shopping Centre',
                             'NW': 'Algor Apartments',
                             'NE': 'Highrise Apartments',
                             'S': 'Google Bridge',
                             'W': 'Train Station',
                             'GROUND': {'a bin ': {'Info': 'Grass grows out of it, the metal base has become one with the vegetation',
                                                   'Takeable': False,
                                                   'Recollectable': False},
                                        'a tyre ': {'Info': 'filled with stagnant water, insects buzz around it as you approach',
                                                    'Takeable': True,
                                                    'Recollectable': False}}},
             'Train Station': {'VIEW': 'The building still stands on one side, the train still stops here, and robots maintain the tracks and train.\nAn obsolete droid asks you for a ticket?',
                               'N': 'Droid Factory',
                               'E': 'City Centre',
                               'S': 'Recycle Plant',
                               'SE': 'Google Bridge',
                               'GROUND': {'a whistle ': {'Info': 'The ticket asking droid has a yellow whistle round its neck',
                                                         'Takeable': True,
                                                         'Recollectable': False}}},
             'Wind Turbines': {'VIEW': '12 Magnificently large, rusty turbines. As you watch a large piece of a turbine blade is blown off into the sea.\n',
                               'E': 'Tram Station',
                               'S': 'Droid Factory',
                               'GROUND': {'flowers': {'Info': 'yellow flowers, smell just as good as they look',
                                                      'Takeable': True,
                                                      'Recollectable': True}}},
             'Shopping Centre':  {'VIEW': 'The glass roof is cracked in numerous places. The escalators fell through the bottom. Ivy grows on all the wall and the other half of the building has fire damage.\nThe building is very dark inside.',
                                  'N': 'Tram Station',
                                  'E': 'Highrise Apartments',
                                  'S': 'City Centre',
                                  'SW': 'Algor Apartments',
                                  'GROUND': {'jewellery ': {'Info': 'lots of dusty jewellery cases, rings pearls, gold teeth',
                                                            'Takeable': True,
                                                            'Recollectable': True},
                                             'perfume ': {'Info': 'smells like raspberry’s',
                                                          'Takeable': True,
                                                          'Recollectable': True}}},
             'Tram Station': {'VIEW': 'A rusted heap of metal, that once was a tram, lies in thick undergrowth.\nThere\'s movement inside, seems like some animal has made it a home.',
                              'E': 'Beach',
                              'S': 'Shopping Centre',
                              'SE': 'Highrise Apartments',
                              'W': 'Wind Turbines',
                              'GROUND': {'ticket machines': {'Info': 'Two yellow boxes with a dark glass screen in the middle',
                                                             'Takeable': False}}},
             'Highrise Apartments': {'VIEW': 'A river now flows from the building’s basement. All floors above it collapsed in. Plants thrive in the bricks that once were the building\'s walls.',
                                     'N': 'Beach',
                                     'NW': 'Tram Station',
                                     'SW': 'City Centre',
                                     'W': 'Shopping Centre',
                                     'GROUND': {'frogs': {'Info': 'Brown slippery and croaking ',
                                                          'Takeable': True,
                                                          'Recollectable': False}}},
             'Beach': {'VIEW': 'Sand and more sand,\nthen the sea that goes as far as a super advanced Droid eye can see.',
                       'S': 'Highrise Apartments',
                       'W': 'Tram Station',
                       'GROUND': {'sand ': {'Info': 'grainy and golden',
                                            'Takeable': True,
                                            'Recollectable': True}}},
             'WaterFall': {'VIEW': 'A muddy marsh prevents you from getting closer, the sound of water is deafening, but you can hardly see the waterfall, through all the trees',
                           'W': 'Power Station',
                           'GROUND': {'water ': {'Info': 'Wet and cold, smells like rain',
                                                 'Takeable': True,
                                                 'Recollectable': True}}},
             'Google Bridge': {'VIEW': 'You can see so much from up here, trees obscure the view of the city centre and you can just make out the ocean, you hear the train passing under the bridge.',
                               'N': 'City Centre',
                               'SE': 'Power Station',
                               'NW': 'Train Station',
                               'S': 'Welcome Bridge',
                               'GROUND': {'moss ': {'Info': 'Thick moss on rocks, soft and rough at the same time',
                                                    'Takeable': False,
                                                    'Recollectable': False}}},
             'Welcome Bridge': {'VIEW': 'The full glory of the waterfall is visible. It is so beautiful; a rainbow runs the length of the water. You take several videos and store them with your protected files',
                                'N': 'Google Bridge',
                                'W': 'Recycle Plant',
                                'E': 'Power Station',
                                'S': 'City Gates',
                                'GROUND': {'moss ': {'Info': 'Thick moss on rocks, soft and rough at the same time',
                                                     'Takeable': False,
                                                     'Recollectable': False}}}
             }
