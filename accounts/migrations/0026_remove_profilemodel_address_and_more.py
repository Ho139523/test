# Generated by Django 5.1.3 on 2025-01-16 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_alter_profilemodel_instagram_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='address',
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='shipping_city',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='shipping_country',
            field=models.CharField(blank=True, choices=[('AW', 'Aruba'), ('AF', 'Afghanistan'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AX', 'Åland Islands'), ('AL', 'Albania'), ('AD', 'Andorra'), ('AE', 'United Arab Emirates'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AS', 'American Samoa'), ('AQ', 'Antarctica'), ('TF', 'French Southern Territories'), ('AG', 'Antigua and Barbuda'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BI', 'Burundi'), ('BE', 'Belgium'), ('BJ', 'Benin'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BF', 'Burkina Faso'), ('BD', 'Bangladesh'), ('BG', 'Bulgaria'), ('BH', 'Bahrain'), ('BS', 'Bahamas'), ('BA', 'Bosnia and Herzegovina'), ('BL', 'Saint Barthélemy'), ('BY', 'Belarus'), ('BZ', 'Belize'), ('BM', 'Bermuda'), ('BO', 'Bolivia, Plurinational State of'), ('BR', 'Brazil'), ('BB', 'Barbados'), ('BN', 'Brunei Darussalam'), ('BT', 'Bhutan'), ('BV', 'Bouvet Island'), ('BW', 'Botswana'), ('CF', 'Central African Republic'), ('CA', 'Canada'), ('CC', 'Cocos (Keeling) Islands'), ('CH', 'Switzerland'), ('CL', 'Chile'), ('CN', 'China'), ('CI', "Côte d'Ivoire"), ('CM', 'Cameroon'), ('CD', 'Congo, The Democratic Republic of the'), ('CG', 'Congo'), ('CK', 'Cook Islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CV', 'Cabo Verde'), ('CR', 'Costa Rica'), ('CU', 'Cuba'), ('CW', 'Curaçao'), ('CX', 'Christmas Island'), ('KY', 'Cayman Islands'), ('CY', 'Cyprus'), ('CZ', 'Czechia'), ('DE', 'Germany'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DK', 'Denmark'), ('DO', 'Dominican Republic'), ('DZ', 'Algeria'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('ER', 'Eritrea'), ('EH', 'Western Sahara'), ('ES', 'Spain'), ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FI', 'Finland'), ('FJ', 'Fiji'), ('FK', 'Falkland Islands (Malvinas)'), ('FR', 'France'), ('FO', 'Faroe Islands'), ('FM', 'Micronesia, Federated States of'), ('GA', 'Gabon'), ('GB', 'United Kingdom'), ('GE', 'Georgia'), ('GG', 'Guernsey'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GN', 'Guinea'), ('GP', 'Guadeloupe'), ('GM', 'Gambia'), ('GW', 'Guinea-Bissau'), ('GQ', 'Equatorial Guinea'), ('GR', 'Greece'), ('GD', 'Grenada'), ('GL', 'Greenland'), ('GT', 'Guatemala'), ('GF', 'French Guiana'), ('GU', 'Guam'), ('GY', 'Guyana'), ('HK', 'Hong Kong'), ('HM', 'Heard Island and McDonald Islands'), ('HN', 'Honduras'), ('HR', 'Croatia'), ('HT', 'Haiti'), ('HU', 'Hungary'), ('ID', 'Indonesia'), ('IM', 'Isle of Man'), ('IN', 'India'), ('IO', 'British Indian Ocean Territory'), ('IE', 'Ireland'), ('IR', 'Iran, Islamic Republic of'), ('IQ', 'Iraq'), ('IS', 'Iceland'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JE', 'Jersey'), ('JO', 'Jordan'), ('JP', 'Japan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KG', 'Kyrgyzstan'), ('KH', 'Cambodia'), ('KI', 'Kiribati'), ('KN', 'Saint Kitts and Nevis'), ('KR', 'Korea, Republic of'), ('KW', 'Kuwait'), ('LA', "Lao People's Democratic Republic"), ('LB', 'Lebanon'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LC', 'Saint Lucia'), ('LI', 'Liechtenstein'), ('LK', 'Sri Lanka'), ('LS', 'Lesotho'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('LV', 'Latvia'), ('MO', 'Macao'), ('MF', 'Saint Martin (French part)'), ('MA', 'Morocco'), ('MC', 'Monaco'), ('MD', 'Moldova, Republic of'), ('MG', 'Madagascar'), ('MV', 'Maldives'), ('MX', 'Mexico'), ('MH', 'Marshall Islands'), ('MK', 'North Macedonia'), ('ML', 'Mali'), ('MT', 'Malta'), ('MM', 'Myanmar'), ('ME', 'Montenegro'), ('MN', 'Mongolia'), ('MP', 'Northern Mariana Islands'), ('MZ', 'Mozambique'), ('MR', 'Mauritania'), ('MS', 'Montserrat'), ('MQ', 'Martinique'), ('MU', 'Mauritius'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('YT', 'Mayotte'), ('NA', 'Namibia'), ('NC', 'New Caledonia'), ('NE', 'Niger'), ('NF', 'Norfolk Island'), ('NG', 'Nigeria'), ('NI', 'Nicaragua'), ('NU', 'Niue'), ('NL', 'Netherlands'), ('NO', 'Norway'), ('NP', 'Nepal'), ('NR', 'Nauru'), ('NZ', 'New Zealand'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PA', 'Panama'), ('PN', 'Pitcairn'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PW', 'Palau'), ('PG', 'Papua New Guinea'), ('PL', 'Poland'), ('PR', 'Puerto Rico'), ('KP', "Korea, Democratic People's Republic of"), ('PT', 'Portugal'), ('PY', 'Paraguay'), ('PS', 'Palestine, State of'), ('PF', 'French Polynesia'), ('QA', 'Qatar'), ('RE', 'Réunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('SA', 'Saudi Arabia'), ('SD', 'Sudan'), ('SN', 'Senegal'), ('SG', 'Singapore'), ('GS', 'South Georgia and the South Sandwich Islands'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('SJ', 'Svalbard and Jan Mayen'), ('SB', 'Solomon Islands'), ('SL', 'Sierra Leone'), ('SV', 'El Salvador'), ('SM', 'San Marino'), ('SO', 'Somalia'), ('PM', 'Saint Pierre and Miquelon'), ('RS', 'Serbia'), ('SS', 'South Sudan'), ('ST', 'Sao Tome and Principe'), ('SR', 'Suriname'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SE', 'Sweden'), ('SZ', 'Eswatini'), ('SX', 'Sint Maarten (Dutch part)'), ('SC', 'Seychelles'), ('SY', 'Syrian Arab Republic'), ('TC', 'Turks and Caicos Islands'), ('TD', 'Chad'), ('TG', 'Togo'), ('TH', 'Thailand'), ('TJ', 'Tajikistan'), ('TK', 'Tokelau'), ('TM', 'Turkmenistan'), ('TL', 'Timor-Leste'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Türkiye'), ('TV', 'Tuvalu'), ('TW', 'Taiwan, Province of China'), ('TZ', 'Tanzania, United Republic of'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('UM', 'United States Minor Outlying Islands'), ('UY', 'Uruguay'), ('US', 'United States'), ('UZ', 'Uzbekistan'), ('VA', 'Holy See (Vatican City State)'), ('VC', 'Saint Vincent and the Grenadines'), ('VE', 'Venezuela, Bolivarian Republic of'), ('VG', 'Virgin Islands, British'), ('VI', 'Virgin Islands, U.S.'), ('VN', 'Viet Nam'), ('VU', 'Vanuatu'), ('WF', 'Wallis and Futuna'), ('WS', 'Samoa'), ('YE', 'Yemen'), ('ZA', 'South Africa'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], max_length=10, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='shipping_home_phone',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Residential Phone Number'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='shipping_line1',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Address Line 1'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='shipping_line2',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Address Line 2'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='shipping_province',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Province'),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='shipping_zip',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Zip Code'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_level',
            field=models.CharField(choices=[('blue', 'کاربر آبی'), ('green', 'کاربر سبز'), ('silver', 'کاربر نقره\u200cای'), ('gold', 'کاربر طلایی'), ('seller', 'کاربر فروشنده')], default='blue', max_length=10),
        ),
        migrations.DeleteModel(
            name='ShippingAddressModel',
        ),
    ]
