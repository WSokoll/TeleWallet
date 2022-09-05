PGDMP     !    	                z        
   teleWallet    13.5    13.5 @               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    26071 
   teleWallet    DATABASE     q   CREATE DATABASE "teleWallet" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United Kingdom.1252';
    DROP DATABASE "teleWallet";
                postgres    false            �            1259    26095    Account    TABLE     {   CREATE TABLE public."Account" (
    id integer NOT NULL,
    active boolean DEFAULT false NOT NULL,
    created_at date
);
    DROP TABLE public."Account";
       public         heap    postgres    false            �            1259    26093    Account_id_seq    SEQUENCE     �   ALTER TABLE public."Account" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Account_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    205            �            1259    26111    Currency    TABLE     �   CREATE TABLE public."Currency" (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    exchange_rate double precision NOT NULL
);
    DROP TABLE public."Currency";
       public         heap    postgres    false            �            1259    26135    CurrencyExchange    TABLE       CREATE TABLE public."CurrencyExchange" (
    id integer NOT NULL,
    user_id integer NOT NULL,
    currency_from integer NOT NULL,
    currency_to integer NOT NULL,
    value_old double precision NOT NULL,
    value_new double precision NOT NULL,
    exchange_date date NOT NULL
);
 &   DROP TABLE public."CurrencyExchange";
       public         heap    postgres    false            �            1259    26133    CurrencyExchange_id_seq    SEQUENCE     �   ALTER TABLE public."CurrencyExchange" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."CurrencyExchange_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    215            �            1259    26109    Currency_id_seq    SEQUENCE     �   ALTER TABLE public."Currency" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Currency_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    209            �            1259    26125    ExternalTransaction    TABLE     %  CREATE TABLE public."ExternalTransaction" (
    id integer NOT NULL,
    transaction_from character varying(500),
    transaction_to integer NOT NULL,
    currency_id integer NOT NULL,
    value double precision NOT NULL,
    transaction_date date NOT NULL,
    name character varying(255)
);
 )   DROP TABLE public."ExternalTransaction";
       public         heap    postgres    false            �            1259    26123    ExternalTransaction_id_seq    SEQUENCE     �   ALTER TABLE public."ExternalTransaction" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."ExternalTransaction_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    213            �            1259    26118    InternalTransaction    TABLE       CREATE TABLE public."InternalTransaction" (
    id integer NOT NULL,
    transaction_from integer NOT NULL,
    transaction_to integer NOT NULL,
    currency_id integer NOT NULL,
    value double precision NOT NULL,
    transaction_date date NOT NULL,
    name character varying(255)
);
 )   DROP TABLE public."InternalTransaction";
       public         heap    postgres    false            �            1259    26116    InternalTransaction_id_seq    SEQUENCE     �   ALTER TABLE public."InternalTransaction" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."InternalTransaction_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    211            �            1259    26086    Role    TABLE     �   CREATE TABLE public."Role" (
    id integer NOT NULL,
    name character varying(80) NOT NULL,
    description character varying(255)
);
    DROP TABLE public."Role";
       public         heap    postgres    false            �            1259    26084    Role_id_seq    SEQUENCE     �   ALTER TABLE public."Role" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Role_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    203            �            1259    26142 
   RolesUsers    TABLE     h   CREATE TABLE public."RolesUsers" (
    id integer NOT NULL,
    user_id integer,
    role_id integer
);
     DROP TABLE public."RolesUsers";
       public         heap    postgres    false            �            1259    26140    RolesUsers_id_seq    SEQUENCE     �   ALTER TABLE public."RolesUsers" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."RolesUsers_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    217            �            1259    26103 
   SubAccount    TABLE     �   CREATE TABLE public."SubAccount" (
    id integer NOT NULL,
    balance double precision DEFAULT 0.0,
    account_id integer NOT NULL,
    currency_id integer NOT NULL
);
     DROP TABLE public."SubAccount";
       public         heap    postgres    false            �            1259    26101    SubAccount_id_seq    SEQUENCE     �   ALTER TABLE public."SubAccount" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."SubAccount_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    207            �            1259    26074    User    TABLE     �  CREATE TABLE public."User" (
    id integer NOT NULL,
    email character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    password character varying(255) NOT NULL,
    last_login_at date,
    current_login_at date,
    last_login_ip character varying(100),
    current_login_ip character varying(100),
    login_count integer,
    active boolean,
    fs_uniquifier character varying(255) NOT NULL,
    confirmed_at date,
    account_id integer NOT NULL
);
    DROP TABLE public."User";
       public         heap    postgres    false            �            1259    26072    User_id_seq    SEQUENCE     �   ALTER TABLE public."User" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."User_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    201                       0    26095    Account 
   TABLE DATA           ;   COPY public."Account" (id, active, created_at) FROM stdin;
    public          postgres    false    205   Q                 0    26111    Currency 
   TABLE DATA           =   COPY public."Currency" (id, name, exchange_rate) FROM stdin;
    public          postgres    false    209   KQ       
          0    26135    CurrencyExchange 
   TABLE DATA           z   COPY public."CurrencyExchange" (id, user_id, currency_from, currency_to, value_old, value_new, exchange_date) FROM stdin;
    public          postgres    false    215   �Q                 0    26125    ExternalTransaction 
   TABLE DATA           �   COPY public."ExternalTransaction" (id, transaction_from, transaction_to, currency_id, value, transaction_date, name) FROM stdin;
    public          postgres    false    213   �Q                 0    26118    InternalTransaction 
   TABLE DATA           �   COPY public."InternalTransaction" (id, transaction_from, transaction_to, currency_id, value, transaction_date, name) FROM stdin;
    public          postgres    false    211   R       �          0    26086    Role 
   TABLE DATA           7   COPY public."Role" (id, name, description) FROM stdin;
    public          postgres    false    203   bR                 0    26142 
   RolesUsers 
   TABLE DATA           <   COPY public."RolesUsers" (id, user_id, role_id) FROM stdin;
    public          postgres    false    217   R                 0    26103 
   SubAccount 
   TABLE DATA           L   COPY public."SubAccount" (id, balance, account_id, currency_id) FROM stdin;
    public          postgres    false    207   �R       �          0    26074    User 
   TABLE DATA           �   COPY public."User" (id, email, name, password, last_login_at, current_login_at, last_login_ip, current_login_ip, login_count, active, fs_uniquifier, confirmed_at, account_id) FROM stdin;
    public          postgres    false    201   �R                  0    0    Account_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public."Account_id_seq"', 2, true);
          public          postgres    false    204                       0    0    CurrencyExchange_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public."CurrencyExchange_id_seq"', 13, true);
          public          postgres    false    214                       0    0    Currency_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public."Currency_id_seq"', 4, true);
          public          postgres    false    208                       0    0    ExternalTransaction_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public."ExternalTransaction_id_seq"', 5, true);
          public          postgres    false    212                       0    0    InternalTransaction_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public."InternalTransaction_id_seq"', 5, true);
          public          postgres    false    210                       0    0    Role_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public."Role_id_seq"', 1, false);
          public          postgres    false    202                       0    0    RolesUsers_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public."RolesUsers_id_seq"', 1, false);
          public          postgres    false    216                       0    0    SubAccount_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public."SubAccount_id_seq"', 4, true);
          public          postgres    false    206                       0    0    User_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public."User_id_seq"', 4, true);
          public          postgres    false    200            _           2606    26100    Account Account_pk 
   CONSTRAINT     T   ALTER TABLE ONLY public."Account"
    ADD CONSTRAINT "Account_pk" PRIMARY KEY (id);
 @   ALTER TABLE ONLY public."Account" DROP CONSTRAINT "Account_pk";
       public            postgres    false    205            i           2606    26139 $   CurrencyExchange CurrencyExchange_pk 
   CONSTRAINT     f   ALTER TABLE ONLY public."CurrencyExchange"
    ADD CONSTRAINT "CurrencyExchange_pk" PRIMARY KEY (id);
 R   ALTER TABLE ONLY public."CurrencyExchange" DROP CONSTRAINT "CurrencyExchange_pk";
       public            postgres    false    215            c           2606    26115    Currency Currency_pk 
   CONSTRAINT     V   ALTER TABLE ONLY public."Currency"
    ADD CONSTRAINT "Currency_pk" PRIMARY KEY (id);
 B   ALTER TABLE ONLY public."Currency" DROP CONSTRAINT "Currency_pk";
       public            postgres    false    209            g           2606    26132 *   ExternalTransaction ExternalTransaction_pk 
   CONSTRAINT     l   ALTER TABLE ONLY public."ExternalTransaction"
    ADD CONSTRAINT "ExternalTransaction_pk" PRIMARY KEY (id);
 X   ALTER TABLE ONLY public."ExternalTransaction" DROP CONSTRAINT "ExternalTransaction_pk";
       public            postgres    false    213            e           2606    26122 *   InternalTransaction InternalTransaction_pk 
   CONSTRAINT     l   ALTER TABLE ONLY public."InternalTransaction"
    ADD CONSTRAINT "InternalTransaction_pk" PRIMARY KEY (id);
 X   ALTER TABLE ONLY public."InternalTransaction" DROP CONSTRAINT "InternalTransaction_pk";
       public            postgres    false    211            [           2606    26090    Role Role_pk 
   CONSTRAINT     N   ALTER TABLE ONLY public."Role"
    ADD CONSTRAINT "Role_pk" PRIMARY KEY (id);
 :   ALTER TABLE ONLY public."Role" DROP CONSTRAINT "Role_pk";
       public            postgres    false    203            ]           2606    26092    Role Role_uq 
   CONSTRAINT     K   ALTER TABLE ONLY public."Role"
    ADD CONSTRAINT "Role_uq" UNIQUE (name);
 :   ALTER TABLE ONLY public."Role" DROP CONSTRAINT "Role_uq";
       public            postgres    false    203            k           2606    26146    RolesUsers RolesUsers_pk 
   CONSTRAINT     Z   ALTER TABLE ONLY public."RolesUsers"
    ADD CONSTRAINT "RolesUsers_pk" PRIMARY KEY (id);
 F   ALTER TABLE ONLY public."RolesUsers" DROP CONSTRAINT "RolesUsers_pk";
       public            postgres    false    217            a           2606    26108    SubAccount SubAccount_pk 
   CONSTRAINT     Z   ALTER TABLE ONLY public."SubAccount"
    ADD CONSTRAINT "SubAccount_pk" PRIMARY KEY (id);
 F   ALTER TABLE ONLY public."SubAccount" DROP CONSTRAINT "SubAccount_pk";
       public            postgres    false    207            W           2606    26081    User User_pk 
   CONSTRAINT     N   ALTER TABLE ONLY public."User"
    ADD CONSTRAINT "User_pk" PRIMARY KEY (id);
 :   ALTER TABLE ONLY public."User" DROP CONSTRAINT "User_pk";
       public            postgres    false    201            Y           2606    26083    User User_uq 
   CONSTRAINT     m   ALTER TABLE ONLY public."User"
    ADD CONSTRAINT "User_uq" UNIQUE (account_id, email, name, fs_uniquifier);
 :   ALTER TABLE ONLY public."User" DROP CONSTRAINT "User_uq";
       public            postgres    false    201    201    201    201            t           2606    26187 )   CurrencyExchange CurrencyExchange_fk_User    FK CONSTRAINT     �   ALTER TABLE ONLY public."CurrencyExchange"
    ADD CONSTRAINT "CurrencyExchange_fk_User" FOREIGN KEY (user_id) REFERENCES public."User"(id);
 W   ALTER TABLE ONLY public."CurrencyExchange" DROP CONSTRAINT "CurrencyExchange_fk_User";
       public          postgres    false    215    2903    201            u           2606    26192 )   CurrencyExchange CurrencyExchange_fk_from    FK CONSTRAINT     �   ALTER TABLE ONLY public."CurrencyExchange"
    ADD CONSTRAINT "CurrencyExchange_fk_from" FOREIGN KEY (currency_from) REFERENCES public."Currency"(id);
 W   ALTER TABLE ONLY public."CurrencyExchange" DROP CONSTRAINT "CurrencyExchange_fk_from";
       public          postgres    false    209    2915    215            v           2606    26197 '   CurrencyExchange CurrencyExchange_fk_to    FK CONSTRAINT     �   ALTER TABLE ONLY public."CurrencyExchange"
    ADD CONSTRAINT "CurrencyExchange_fk_to" FOREIGN KEY (currency_to) REFERENCES public."Currency"(id);
 U   ALTER TABLE ONLY public."CurrencyExchange" DROP CONSTRAINT "CurrencyExchange_fk_to";
       public          postgres    false    209    2915    215            s           2606    26182 3   ExternalTransaction ExternalTransaction_fk_Currency    FK CONSTRAINT     �   ALTER TABLE ONLY public."ExternalTransaction"
    ADD CONSTRAINT "ExternalTransaction_fk_Currency" FOREIGN KEY (currency_id) REFERENCES public."Currency"(id);
 a   ALTER TABLE ONLY public."ExternalTransaction" DROP CONSTRAINT "ExternalTransaction_fk_Currency";
       public          postgres    false    2915    209    213            r           2606    26177 -   ExternalTransaction ExternalTransaction_fk_to    FK CONSTRAINT     �   ALTER TABLE ONLY public."ExternalTransaction"
    ADD CONSTRAINT "ExternalTransaction_fk_to" FOREIGN KEY (transaction_to) REFERENCES public."User"(id);
 [   ALTER TABLE ONLY public."ExternalTransaction" DROP CONSTRAINT "ExternalTransaction_fk_to";
       public          postgres    false    213    2903    201            q           2606    26172 3   InternalTransaction InternalTransaction_fk_Currency    FK CONSTRAINT     �   ALTER TABLE ONLY public."InternalTransaction"
    ADD CONSTRAINT "InternalTransaction_fk_Currency" FOREIGN KEY (currency_id) REFERENCES public."Currency"(id);
 a   ALTER TABLE ONLY public."InternalTransaction" DROP CONSTRAINT "InternalTransaction_fk_Currency";
       public          postgres    false    211    2915    209            o           2606    26162 /   InternalTransaction InternalTransaction_fk_from    FK CONSTRAINT     �   ALTER TABLE ONLY public."InternalTransaction"
    ADD CONSTRAINT "InternalTransaction_fk_from" FOREIGN KEY (transaction_from) REFERENCES public."User"(id);
 ]   ALTER TABLE ONLY public."InternalTransaction" DROP CONSTRAINT "InternalTransaction_fk_from";
       public          postgres    false    201    2903    211            p           2606    26167 -   InternalTransaction InternalTransaction_fk_to    FK CONSTRAINT     �   ALTER TABLE ONLY public."InternalTransaction"
    ADD CONSTRAINT "InternalTransaction_fk_to" FOREIGN KEY (transaction_to) REFERENCES public."User"(id);
 [   ALTER TABLE ONLY public."InternalTransaction" DROP CONSTRAINT "InternalTransaction_fk_to";
       public          postgres    false    211    2903    201            x           2606    26207    RolesUsers RolesUsers_fk_Role    FK CONSTRAINT     �   ALTER TABLE ONLY public."RolesUsers"
    ADD CONSTRAINT "RolesUsers_fk_Role" FOREIGN KEY (role_id) REFERENCES public."Role"(id);
 K   ALTER TABLE ONLY public."RolesUsers" DROP CONSTRAINT "RolesUsers_fk_Role";
       public          postgres    false    2907    203    217            w           2606    26202    RolesUsers RolesUsers_fk_User    FK CONSTRAINT     �   ALTER TABLE ONLY public."RolesUsers"
    ADD CONSTRAINT "RolesUsers_fk_User" FOREIGN KEY (user_id) REFERENCES public."User"(id);
 K   ALTER TABLE ONLY public."RolesUsers" DROP CONSTRAINT "RolesUsers_fk_User";
       public          postgres    false    201    217    2903            n           2606    26157     SubAccount SubAccount_fk_Account    FK CONSTRAINT     �   ALTER TABLE ONLY public."SubAccount"
    ADD CONSTRAINT "SubAccount_fk_Account" FOREIGN KEY (account_id) REFERENCES public."Account"(id);
 N   ALTER TABLE ONLY public."SubAccount" DROP CONSTRAINT "SubAccount_fk_Account";
       public          postgres    false    2911    205    207            m           2606    26152 !   SubAccount SubAccount_fk_Currency    FK CONSTRAINT     �   ALTER TABLE ONLY public."SubAccount"
    ADD CONSTRAINT "SubAccount_fk_Currency" FOREIGN KEY (currency_id) REFERENCES public."Currency"(id);
 O   ALTER TABLE ONLY public."SubAccount" DROP CONSTRAINT "SubAccount_fk_Currency";
       public          postgres    false    2915    209    207            l           2606    26147    User User_fk_Account    FK CONSTRAINT     ~   ALTER TABLE ONLY public."User"
    ADD CONSTRAINT "User_fk_Account" FOREIGN KEY (account_id) REFERENCES public."Account"(id);
 B   ALTER TABLE ONLY public."User" DROP CONSTRAINT "User_fk_Account";
       public          postgres    false    205    2911    201                   x�3�,�4202�5��5��2B���qqq r�         (   x�3�L--�4�3��2�,-N1�9r�8�b���� �n?      
   1   x�34�4�4�4�42�4�3�FF����\��09NK=c�=... �	,         ;   x�3�,)H��4�4�44ֳ��4202�5��50�(��mJL�/O��L�2%Iu� �n:         C   x�3�4�4�4B###]K]SΒ����J����Ԝ�r��|�Ģ�D.S��+KJ�6q��qqq �Wd      �      x������ � �            x������ � �         6   x�ɱ�@��A�d/�_8�Eg�"2��0��V�bIÏ��{>����J      �   �   x�m�MO�0 ��s�+v�u]?&����eٖ]
�R���ɯ��Q�7����]Oo?���w��&Q3� ���\�ݍ�����1[�[�g���,p|rJp���i�ϩN��^5#������&7�"B�C�;�8`��)q���/�Ƅ���d��9v��*�v6��u���I]�hnNA�#��b}�
���T�k���f��Go1�kg�����	b��!��|SV     